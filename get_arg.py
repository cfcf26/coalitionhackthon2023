import argparse

parser = argparse.ArgumentParser()
parser.add_argument("cmd",type=str, nargs=argparse.REMAINDER)
args = parser.parse_args()

cmd = None
opt = None

if args.cmd:
	cmd = args.cmd[0]
	if len(args.cmd) > 1:
		opt = args.cmd[1]
else:
	print("Error: At least one argument is required.")
	parser.print_help()
	exit(1)

if opt == None:
	opt = "default"

# print("cmd: %s" % cmd)
# print("opt: %s" % opt)


