import concurrent.futures
from functools import partial


def stage1_generate():
    """Stage 1: Generate numbers from 1 to 100"""
    return range(1, 101)


def stage2_filter(number):
    """Stage 2: Filter even numbers"""
    if number % 2 == 0:
        return number
    return None


def stage3_square(number):
    """Stage 3: Square the number"""
    if number is not None:
        return number ** 2
    return None


def stage4_output(numbers):
    """Stage 4: Output the results"""
    valid_numbers = [num for num in numbers if num is not None]
    print("Pipeline Results (Parallel Processing):")
    print("-------------------------------------")
    for num in valid_numbers:
        print(num)
    return valid_numbers


def run_parallel_pipeline():
    """Execute the pipeline stages in parallel"""
    # Generate initial numbers
    numbers = stage1_generate()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Stage 2: Filter even numbers in parallel
        filtered_numbers = list(executor.map(stage2_filter, numbers))

        # Stage 3: Square numbers in parallel
        squared_numbers = list(executor.map(stage3_square, filtered_numbers))

    # Stage 4: Output results
    final_results = stage4_output(squared_numbers)
    return final_results


if __name__ == "__main__":
    print("Running number processing pipeline with parallel processing...")
    results = run_parallel_pipeline()
    print("\nParallel pipeline execution completed!")