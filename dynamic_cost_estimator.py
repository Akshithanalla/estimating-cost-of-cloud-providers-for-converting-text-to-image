class CostEstimator:
    def __init__(self, storage_cost_per_gb, processing_cost_per_request, bandwidth_cost_per_gb):
        self.storage_cost_per_gb = storage_cost_per_gb
        self.processing_cost_per_request = processing_cost_per_request
        self.bandwidth_cost_per_gb = bandwidth_cost_per_gb

    def estimate_cost(self, text_length, image_size, image_format, request_count):
        # Calculate storage cost (assuming uncompressed image is stored)
        image_size_bytes = image_size[0] * image_size[1] * 3  # Assuming RGB image format
        image_size_gb = image_size_bytes / (1024 * 1024 * 1024)  # Convert bytes to gigabytes
        storage_cost = self.storage_cost_per_gb * image_size_gb

        # Calculate processing cost
        processing_cost = self.processing_cost_per_request * request_count

        # Calculate bandwidth cost (assuming image is served to users)
        bandwidth_cost = self.bandwidth_cost_per_gb * image_size_gb

        # Total cost
        total_cost = storage_cost + processing_cost + bandwidth_cost

        return total_cost

def main():
    # Initialize cost estimator with sample pricing information
    cost_estimator = CostEstimator(storage_cost_per_gb=0.01,  # $0.01 per GB storage per month
                                   processing_cost_per_request=0.001,  # $0.001 per request
                                   bandwidth_cost_per_gb=0.05)  # $0.05 per GB bandwidth per month

    # Get user input for text, image file type, image size, and request count
    text = input("Enter text: ")
    image_format = input("Enter image format (e.g., PNG, JPEG): ")
    image_width = int(input("Enter image width (in pixels): "))
    image_height = int(input("Enter image height (in pixels): "))
    request_count = int(input("Enter request count: "))

    # Calculate image size based on width and height
    image_size = (image_width, image_height)

    # Estimate cost based on user input
    total_cost = cost_estimator.estimate_cost(len(text), image_size, image_format, request_count)
    print(f"Estimated total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
