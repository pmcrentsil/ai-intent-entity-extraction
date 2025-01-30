import openai
import argparse
import time
from openai import AzureOpenAI
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import json
import transcripts  # Importing conversation data from transcripts.py

# Initialize Azure OpenAI Service
azure_endpoint = ""
api_key = ""

# Initialize the AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version="2024-06-01"
)

MODEL = "gpt-4o-mini"  # Model to use

# Function to process transcription and extract results
def process_transcription(system_message, transcript, entities):
    try:
        # Construct the message payload
        messages = [
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": (
                    f"Given the following call transcript: {transcript}. "
                    f"Extract the following entities: call intent (as defined by the intents in the system message), "
                    f"{entities}. Output the entities in JSON key-value format."
                )
            }
        ]
        
        # Start processing time
        start_time = time.time()

        # Call the Azure OpenAI ChatCompletion API
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        # Measure processing time
        processing_time = time.time() - start_time
        
        # Extract the LLM's response
        llm_response = response.choices[0].message.content.strip()

        # Ensure the output is in JSON format
        try:
            result = json.loads(llm_response)
        except json.JSONDecodeError:
            # If not valid JSON, wrap the response in a JSON structure
            result = {"extracted_data": llm_response}

        return result, processing_time
    except Exception as e:
        print(f"Error while processing the transcription: {e}")
        return {"error": str(e)}, 0

# Wrapper function to simulate real-time streaming
def simulate_real_time(system_message, conversation, entities):
    conversation_context = ""  # Keep track of what’s been said so far
    extracted_results = []  # Store extracted intents/entities
    turn_count = 0
    total_processing_time = 0  # Track total processing time

    for turn in conversation:
        turn_count += 1
        conversation_context += turn + " "  # Append to conversation memory
        
        print(f"\nProcessing Turn {turn_count}: {turn.strip()}...\n")
        result, turn_processing_time = process_transcription(system_message, conversation_context.strip(), entities)
        
        # Append extracted data for each turn
        extracted_results.append({
            "turn": turn_count, 
            "data": result,
            "turn_processing_time": f"{turn_processing_time:.2f} seconds"
        })

        # Accumulate total processing time
        total_processing_time += turn_processing_time

        # Simulate real-time delay
        time.sleep(3)  # Wait 3 seconds to mimic real-time conversation
        
    return {
        "total_turns": turn_count,
        "total_processing_time": f"{total_processing_time:.2f} seconds",
        "extracted_data": extracted_results
    }

# Main function
def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Simulate real-time call transcription processing.")
    parser.add_argument('--intents', type=str, required=True, help="List of call intents to identify (comma-separated)")
    parser.add_argument('--entities', type=str, required=True, help="Entities to extract (comma-separated)")
    parser.add_argument('--output-format', type=str, choices=['json', 'text'], default='json', help="Output format")
    
    args = parser.parse_args()
    
    # Prepare system message
    system_message = (
        f"You are a helpful assistant. Please structure the date in date/month/year format. These are the call intents that I would like you to identify "
        f"from the given call transcriptions: {args.intents}."
    )
    
    # Measure processing time
    start_time = time.time()
    
    # Simulate real-time conversation processing using transcripts.py data
    result = simulate_real_time(system_message, transcripts.MULTI_TURN_CONVERSATION, args.entities)
    
    # Output the result
    if args.output_format == "json":
        print(json.dumps(result, indent=4))
    else:
        print(result)
    
    # Print total script processing time
    latency = time.time() - start_time
    print(f"\nTotal Turns: {result['total_turns']}")
    print(f"Total Processing Time: {result['total_processing_time']}")
    print(f"Script Execution Time: {latency:.2f} seconds")

if __name__ == "__main__":
    main()







