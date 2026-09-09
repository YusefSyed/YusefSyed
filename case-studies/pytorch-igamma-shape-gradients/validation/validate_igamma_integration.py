"""Compare real PyTorch autograd outputs with the frozen independent corpus."""
import argparse
from collections import Counter
from decimal import Decimal as D, getcontext
import hashlib
import json
import math
from pathlib import Path
import struct
import sys

import torch

parser = argparse.ArgumentParser()
parser.add_argument('--device', choices=['cpu', 'cuda'], required=True)
parser.add_argument('--cases', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
if args.device == 'cuda' and not torch.cuda.is_available():
    sys.exit('CUDA unavailable; refusing CPU fallback.')
getcontext().prec = 120
mu = D(2) ** -1074
data = json.loads(args.cases.read_text())
cases = [r for r in data['rows'] if r['kind'] == 0]
def value(bits):
    return struct.unpack('>d', struct.pack('>Q', bits))[0]

results = []
for op_name, shape_sign in [('igamma', -1), ('igammac', 1)]:
    av = torch.tensor([value(r['a_bits']) for r in cases], dtype=torch.float64, device=args.device)
    xv = torch.tensor([value(r['x_bits']) for r in cases], dtype=torch.float64, device=args.device)
    a = torch.stack((av, torch.ones_like(av)), dim=1)[:, 0].detach().requires_grad_()
    x = torch.stack((torch.ones_like(xv), xv), dim=1)[:, 1]
    forward = getattr(torch, op_name)(a, x)
    gradient = torch.autograd.grad(forward.sum(), a)[0]
    if args.device == 'cuda':
        torch.cuda.synchronize()
    actual_values = (shape_sign * gradient).detach().cpu().tolist()
    forward_values = forward.detach().cpu().tolist()
    rows = []
    for case, actual, primal in zip(cases, actual_values, forward_values):
        details = {}
        if case['category'] == 'numerical':
            ref = D(case['reference'])
            rounded = float(ref)
            error = abs(D.from_float(actual) - ref) if math.isfinite(actual) else D('Infinity')
            spacing = D.from_float(math.ulp(rounded))
            if rounded >= sys.float_info.min and math.frexp(rounded)[0] == 0.5 and ref < D.from_float(rounded):
                spacing = max(mu, spacing / 2)
            allowed = D('5e-12') * abs(ref) + mu
            if ref >= D.from_float(sys.float_info.min):
                allowed = min(allowed, D('5e-13') * abs(ref))
            if 0 < ref < D(-700).exp():
                allowed = min(allowed, 4 * spacing)
            classification = actual == 0 if rounded == 0 else math.isfinite(actual) and actual > 0
            passed = classification and error <= allowed
            details = dict(absolute_error=str(error), allowed_error=str(allowed))
        else:
            expected = float.fromhex(case['expected_hex'])
            passed = math.isnan(actual) if math.isnan(expected) else actual == expected
        rows.append(dict(**case, derivative_q_hex=actual.hex(), primal_hex=primal.hex(),
                         passed=passed, **details))
    results.append(dict(operator=op_name, grad_fn=type(forward.grad_fn).__name__,
                        input_noncontiguous=not a.is_contiguous() and not x.is_contiguous(),
                        failures=sum(not r['passed'] for r in rows), rows=rows))

report = dict(device=args.device, torch_version=torch.__version__,
              torch_file=torch.__file__, torch_git_version=torch.version.git_version,
              cuda_version=torch.version.cuda,
              gpu=torch.cuda.get_device_name() if args.device == 'cuda' else None,
              counts=dict(Counter(r['category'] for r in cases)),
              case_sha256=hashlib.sha256(args.cases.read_bytes()).hexdigest(),
              total_outputs=len(cases)*2, failures=sum(r['failures'] for r in results),
              results=results)
args.output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k:v for k,v in report.items() if k!='results'}, indent=2))
for result in results:
    for row in result['rows']:
        if not row['passed']:
            print('FAIL', result['operator'], json.dumps(row))
sys.exit(1 if report['failures'] else 0)
