import traceback
import asyncio

'''def run_user_code(code: str, input_data: list):
    try:

        namespace = {}
        exec(code, namespace)
        result = namespace["solve_problem"](*input_data)
        
        return result, None
    
    except Exception as e:
        error_message = traceback.format_exc()

        return None, error_message'''


async def run_user_code_async(code: str, input_data: list, timeout: int = 15):
    try:
        namespace = {}
        exec(code, namespace)
        
        result = await asyncio.wait_for(
            asyncio.to_thread(namespace["solve_problem"], *input_data),
            timeout=timeout
        )
        return result, None
    except asyncio.TimeoutError:
        return None, "Execution timed out"
    except Exception as e:
        error_message = traceback.format_exc()
        return None, error_message
    finally:
        del namespace


async def validate_code(code: str, test_cases: list):
    results = []
    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["output"]
        
        actual_output, error = await run_user_code_async(code, input_data)
        
        if error:
            results.append({
                "input": input_data,
                "expected_output": expected_output,
                "actual_output": None,
                "error": error,
                "passed": False
            })
        else:
            passed = actual_output == expected_output
            results.append({
                "input": input_data,
                "expected_output": expected_output,
                "actual_output": actual_output,
                "error": None,
                "passed": passed
            })
    
    return results