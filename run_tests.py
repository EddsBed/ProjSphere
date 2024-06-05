import subprocess


def run_test_cases():
    TcBoundsSucceed = [['3',28.27433388230813449126799241639674, 28.27433388230813449126799241639675]]
    TcBoundsFail = [['-1', 'Error: Received negative number']]
    TcParsingSucceed = [['1',1.04719755119659763131778618117096, 1.04719755119659763131778618117097], ['1.1',1.39381994064267189514794154092669, 1.3938199406426718951479415409267], ['0.9',0.76340701482231976271464191086125, 0.76340701482231976271464191086126], ['.9',0.76340701482231976271464191086125, 0.76340701482231976271464191086126]]
    TcParsingFail = [['a', 'Error, invalid input' ],['one','Error, invalid input']]

    for i in range(0, len(TcBoundsSucceed)):
        resultStr = subprocess.run(["./bin/Foo",  TcBoundsSucceed[i][0]], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text=True)
        assert resultStr is not None, "Failed to run"
        assert resultStr.stdout is not None or '', "Failed to Receive Output"
        resultInt=float(resultStr.stdout.strip())
        assert TcBoundsSucceed[i][1] <= resultInt <= TcBoundsSucceed[i][2], "Failed: Expected a value between" + TcBoundsSucceed[i][1] + " and " + TcBoundsSucceed[i][2] + "But received " + resultInt + '\n'

    for i in range(0,len(TcParsingSucceed)):
        resultStr = subprocess.run(["./bin/Foo",TcParsingSucceed[i][0]], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text=True)
        assert resultStr is not None, "Failed to run"
        assert resultStr.stdout is not None, "Failed to Receive Output"
        resultInt=float(resultStr.stdout.strip())
        assert TcParsingSucceed[i][1] <= resultInt <= TcParsingSucceed[i][2], "Failed: Expected a value between" + TcParsingSucceed[i][1] + " and " + TcParsingSucceed[i][2] + "But received " + resultInt + '\n'

    for i in range(0,len(TcBoundsFail)):
        resultStr = subprocess.run(["./bin/Foo",TcBoundsFail[i][0]], stdout = subprocess.PIPE, stderr = subprocess.PIPE,  text=True)
        assert resultStr is not None, "Failed to run"
        assert resultStr.stderr == TcBoundsFail[i][1], "Failed, expected " + TcBoundsFail[i][1] + "But received " + resultStr.stderr + '\n'
    
    for i in range(0,len(TcParsingFail)):
        resultStr = subprocess.run(["./bin/Foo", TcParsingFail[i][0]], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text=True)
        assert resultStr is not None, "Failed to run"
        assert resultStr.stderr == TcParsingFail[i][1], "Failed, expected " + TcParsingFail[i][1] + "But received " + resultStr.stderr + '\n'


if __name__ == "__main__":
    run_test_cases()