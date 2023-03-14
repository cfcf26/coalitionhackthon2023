import subprocess
import sys
import get_arg as args

if args.opt == "default":
	result = subprocess.run(['open', args.cmd, sys], stdout=subprocess.PIPE)
# result = subprocess.run(['open', args.cmd, args.opt], stdout=subprocess.PIPE)

# 결과 출력
print(result.stdout.decode('utf-8'))