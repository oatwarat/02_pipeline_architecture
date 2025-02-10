def stage1_generate():
    """Stage 1: Generate numbers from 1 to 100"""
    return range(1, 101)

def stage2_filter(numbers):
    """Stage 2: Filter even numbers"""
    return [num for num in numbers if num % 2 == 0]

def stage3_square(numbers):
    """Stage 3: Square the even numbers"""
    return [num ** 2 for num in numbers]

def stage4_output(numbers):
    """Stage 4: Output the results"""
    print("Pipeline Results:")
    print("----------------")
    for num in numbers:
        print(num)
    return numbers

def run_pipeline():
    """Execute the pipeline stages sequentially"""
    numbers = stage1_generate()
    filtered_numbers = stage2_filter(numbers)
    squared_numbers = stage3_square(filtered_numbers)
    final_results = stage4_output(squared_numbers)
    return final_results

if __name__ == "__main__":
    print("Running number processing pipeline...")
    results = run_pipeline()
    print("\nPipeline execution completed!")