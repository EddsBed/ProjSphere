import subprocess


def run_test_cases():
    TcBoundsSucceed = [[]]
    TcBoundsFail = [[]]
    TcParsingSucceed = [[]]
    TcParsingFail = [[]]

    for i in len(TcBoundsSucceed):
        resultStr = subprocess.run(["./Foo"], input = TcBoundsSucceed[i][0], stdout = subprocess.PIPE, text=True)
        assert resultStr is not None, "Failed to run"
        assert resultStr.stdout is not None, "Failed to Receive Output"
        resultInt=float(resultStr.stdout.strip())
        assert TcBoundsSucceed[i][1] <= resultInt <= TcBoundsSucceed[i][2], "Failed: Expected a value between" + TcBoundsSucceed[i][1] + " and " + TcBoundsSucceed[i][2] + "But received " + resultInt + '\n'

    for i in len(TcParsingSucceed):
        resultStr = subprocess.run(["./Foo"], input = TcParsingSucceed[i][0], stdout = subprocess.PIPE, text=True)
        assert resultStr is not None, "Failed to run"
        assert resultStr.stdout is not None, "Failed to Receive Output"
        resultInt=float(resultStr.stdout.strip())
        assert TcParsingSucceed[i][1] <= resultInt <= TcParsingSucceed[i][2], "Failed: Expected a value between" + TcParsingSucceed[i][1] + " and " + TcParsingSucceed[i][2] + "But received " + resultInt + '\n'

    for i in len(TcBoundsFail):
        resultStr = subprocess.run(["./Foo"], input = TcBoundsFail[i][0], stdout = subprocess.PIPE, text=True)
        assert resultStr is not None, "Failed to run"
        assert resultStr == TcBoundsFail[i][1], "Failed, expected " + TcBoundsFail[i][1] + "But received " + resultStr + '\n'
    
    for i in len(TcParsingFail):
        resultStr = subprocess.run(["./Foo"], input = TcParsingFail[i][0], stdout = subprocess.PIPE, text=True)
        assert resultStr is not None, "Failed to run"
        assert TcParsingFail[i][1] == resultStr, "Failed, expected " + TcParsingFail[i][1] + "But received " + resultStr + '\n'


if __name__ == "__main__":
    run_test_cases()