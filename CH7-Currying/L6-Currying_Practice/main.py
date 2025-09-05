def new_resizer(max_width, max_height):
    def set_min_size(min_width=0, min_height=0):
        # Validate minimum size constraints
        if min_width > max_width or min_height > max_height:
            raise ValueError("minimum size cannot exceed maximum size")

        def resize_image(width, height):
            # Apply mathematical constraints to dimensions
            new_width = max(min_width, min(width, max_width))
            new_height = max(min_height, min(height, max_height))
            return new_width, new_height

        return resize_image
    return set_min_size

