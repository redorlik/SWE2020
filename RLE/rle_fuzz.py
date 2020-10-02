from fuzzing.fuzzer import FuzzExecutor




inpu_ls = ['enkoding.txt']

target = ['python rle-py -e']

number_of_runs = 13

def test():
    print("Starting test")
    fuzz_executor = FuzzExecutor(target, inpu_ls)
    fuzz_executor.run_test(number_of_runs)
    return fuzz_executor.stats

def main():
    stats = test()
    print(stats)



if __name__ == '__main__':

    main()
