def calculate_total_cost_scenario1(text_prompt, image_width, image_height, image_format):
    # Constants based on Scenario 1
    hourly_rate_usd = 0.10  # Hourly rate for AWS EC2 instance in USD
    processing_time_hours = 0.0833  # Processing time in hours
    additional_cost_usd = 0.002  # Additional cost for data transfer in USD
    
    # Convert hourly rate from USD to INR
    compute_resources_inr = hourly_rate_usd * 75
    
    # Calculate processing cost in USD and convert to INR
    processing_cost_usd = hourly_rate_usd * processing_time_hours
    processing_cost_inr = processing_cost_usd * 75
    
    # Convert additional cost from USD to INR
    additional_cost_inr = additional_cost_usd * 75
    
    # Adjust cost based on prompt complexity
    prompt_complexity_factor = len(text_prompt) / 100  # Example: Increase cost for longer prompts
    
    # Adjust cost based on image size
    image_size_factor = (image_width * image_height) / (800 * 600)  # Example: Increase cost for larger images
    
    # Adjust cost based on image format
    if image_format.upper() == 'JPEG':
        image_format_cost_inr = 0.25  # Example: Additional cost for JPEG format
    else:
        image_format_cost_inr = 0
    
    # Total cost calculation for Scenario 1
    total_cost_inr = (compute_resources_inr + processing_cost_inr + additional_cost_inr) * \
                     (1 + prompt_complexity_factor + image_size_factor + image_format_cost_inr)
    
    return total_cost_inr

def calculate_total_cost_scenario2(text_prompt, image_width, image_height, image_format):
    # Compute Resource Costs
    hourly_rate = 0.0464
    compute_cost = hourly_rate

    # Storage Costs
    storage_rate = 0.023 / 1000  # Convert from GB/month to GB/hour
    data_volume = (image_width * image_height) / (800 * 600) * 0.05  # Convert from MB to GB
    storage_duration = 1  # month
    storage_cost = storage_rate * data_volume * storage_duration

    # Data Transfer Costs
    data_transfer_rate = 0.01 / 1000  # Convert from $/GB to $/MB
    data_transfer_volume = 10 / 1000  # Convert from MB to GB
    data_transfer_cost = data_transfer_rate * data_transfer_volume

    # AI Model Costs
    ai_model_cost_per_image = 500 / (1 * 720)  # Assuming 1 image per hour, 720 hours in a month
    ai_model_cost = ai_model_cost_per_image * (len(text_prompt) / 100)  # Example: Increase cost for longer prompts

    # Total Estimated Cost
    total_cost = (compute_cost + storage_cost + data_transfer_cost + ai_model_cost)
    return total_cost


if __name__ == "__main__":
    text_prompt = input("Enter the text prompt: ")
    image_width = int(input("Enter the image width in pixels: "))
    image_height = int(input("Enter the image height in pixels: "))
    image_format = input("Enter the image format (JPEG, PNG, etc.): ")

    scenario1_cost = calculate_total_cost_scenario1(text_prompt, image_width, image_height, image_format)
    scenario2_cost = calculate_total_cost_scenario2(text_prompt, image_width, image_height, image_format)
    
    print("Scenario 1 Total Cost: ₹", round(scenario1_cost, 2))
    print("Scenario 2 Total Cost: $", round(scenario2_cost, 4))
