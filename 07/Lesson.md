# Functions Practice

Doc2Doc should seamlessly convert [hex](https://en.wikipedia.org/wiki/Hexadecimal) [triplet color codes](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet) to RGB values. Hex colors are an efficient means of representing color with only 6 characters. RGB values combine red, green and blue light to electronically display the entire color spectrum.

## Assignment

Debug the `hex_to_rgb` function. `hex_to_rgb` should take a hex triplet color code and return three integers for the RGB values using [int()](https://docs.python.org/3/library/functions.html#int). One of the arguments used in `int()` is incorrect, examine the documentation to see how to convert hexadecimal values.

Use the provided `is_hexadecimal` function inside of `hex_to_rgb` to check if its input is valid. If the input is not a six character long hexadecimal string, raise an exception `"not a hex color string"`.

Example:

```python
red_val, green_val, blue_val = hex_to_rgb("A020F0")

print(red_val)
# prints 160

print(green_val)
# prints 32

print(blue_val)
# prints 240
```

![Hex to RGB Conversion](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/AoiBN8T-491x285.png)

---

## Detailed Explanation

### Understanding Hex Colors and RGB

**Hexadecimal colors** represent colors using 6 characters that encode Red, Green, and Blue values:

- **Format**: `"RRGGBB"` (each pair represents one color component)
- **Characters**: 0-9 and A-F (hexadecimal digits)
- **Example**: `"A020F0"` breaks down as:
  - `A0` = Red component (160 in decimal)
  - `20` = Green component (32 in decimal)  
  - `F0` = Blue component (240 in decimal)

### Why Hexadecimal?
- **Compact**: 6 characters vs "rgb(160, 32, 240)"
- **Web standard**: Used in CSS, HTML, design tools
- **Efficient**: Each pair represents 0-255 range in just 2 characters

### The Conversion Process

**Step-by-step breakdown** of `"A020F0"`:

1. **Split into pairs**: `"A0"`, `"20"`, `"F0"`
2. **Convert each pair from hex to decimal**:
   - `"A0"` (hex) → 160 (decimal)
   - `"20"` (hex) → 32 (decimal)  
   - `"F0"` (hex) → 240 (decimal)

**How hex-to-decimal conversion works**:
- `A0` = (A × 16¹) + (0 × 16⁰) = (10 × 16) + (0 × 1) = 160
- `20` = (2 × 16¹) + (0 × 16⁰) = (2 × 16) + (0 × 1) = 32
- `F0` = (F × 16¹) + (0 × 16⁰) = (15 × 16) + (0 × 1) = 240

### The Programming Challenge

This exercise teaches you to:

1. **Debug existing code** - find the bug in the `int()` function usage
2. **Input validation** - use `is_hexadecimal()` to check valid input
3. **Error handling** - raise exceptions for invalid input
4. **String slicing** - extract color components from the 6-character string
5. **Number base conversion** - convert hex strings to decimal integers

### Key Python Concepts

**The `int()` function with base parameter:**
```python
# Wrong way (likely the bug to find):
int("A0")  # Error! Python doesn't know this is hex

# Correct way:
int("A0", 16)  # Tells Python to interpret as base-16 (hexadecimal)
```

**String slicing for color extraction:**
```python
hex_color = "A020F0"
red_hex = hex_color[0:2]    # "A0"
green_hex = hex_color[2:4]  # "20"  
blue_hex = hex_color[4:6]   # "F0"
```

**Complete conversion example:**
```python
def hex_to_rgb(hex_color):
    # Extract each color component (2 characters each)
    red_hex = hex_color[0:2]
    green_hex = hex_color[2:4]
    blue_hex = hex_color[4:6]
    
    # Convert from hex to decimal using base 16
    red = int(red_hex, 16)
    green = int(green_hex, 16)
    blue = int(blue_hex, 16)
    
    return red, green, blue
```

### Input Validation and Error Handling

The exercise requires proper validation:

```python
def hex_to_rgb(hex_color):
    # Check if input is valid hexadecimal
    if not is_hexadecimal(hex_color):
        raise Exception("not a hex color string")
    
    # Check if input is exactly 6 characters
    if len(hex_color) != 6:
        raise Exception("not a hex color string")
    
    # Perform conversion...
```

### Real-World Applications

This skill is useful for:
- **Web development**: Converting between color formats
- **UI design tools**: Processing color palettes  
- **Data visualization**: Converting color specifications in charts and graphs
- **Game development**: Handling color assets and themes
- **Image processing**: Working with pixel color values
- **AI applications**: Processing color data in computer vision tasks

### Debugging Approach

When debugging the provided function:
1. **Identify the `int()` usage** - look for missing base parameter
2. **Test with the example** - `"A020F0"` should return (160, 32, 240)
3. **Add input validation** - use the provided `is_hexadecimal()` function
4. **Handle edge cases** - wrong length strings, invalid characters
5. **Test error conditions** - ensure exceptions are raised properly

This debugging process mirrors the systematic approach used in AI development - when your models produce unexpected outputs, you trace through each transformation step to identify where the logic fails.

---

## Advanced Debugging: Two-Stage Validation Explained

### The Core Problem: Type Safety in Validation

When implementing the `hex_to_rgb` function, a critical issue emerges: **you cannot call `len()` on non-string types**. This creates a fundamental challenge in input validation.

### Why Single-Stage Validation Fails

**Problematic approach:**
```python
# This WILL crash on certain inputs!
if not isinstance(hex_color, str) or not is_hexadecimal(hex_color) or len(hex_color) != 6:
    raise Exception("not a hex color string")
```

**What happens with `hex_color = 1000000` (integer):**
1. `isinstance(1000000, str)` → `False`
2. `not False` → `True`
3. Python evaluates the entire condition and calls `len(1000000)`
4. **Result:** `TypeError: object of type 'int' has no len()`

**The problem:** Even though the first condition is `True`, Python still evaluates `len(hex_color)`, causing a crash with the wrong exception type and message.

### The Two-Stage Solution

**Safe approach with separated validation:**
```python
# Stage 1: Type safety check
if not isinstance(hex_color, str):
    raise Exception("not a hex color string")

# Stage 2: String content validation (safe now!)
if not is_hexadecimal(hex_color) or len(hex_color) != 6:
    raise Exception("not a hex color string")
```

### Why Two Stages Work

**Stage 1 - Type Safety:**
- Purpose: "Is this even a string?"
- Handles: integers, None, lists, etc.
- Example: `1000000` → Not a string → Exception raised immediately

**Stage 2 - Content Validation:**
- Purpose: "Now that we know it's a string, is it valid hex?"
- Safely calls: `len(hex_color)` and `is_hexadecimal(hex_color)`
- Example: `"Hello!"` → Invalid hex → Exception raised

### Alternative Valid Approaches

**Option A (as implemented):**
```python
if not isinstance(hex_color, str):
    raise Exception("not a hex color string")
if not is_hexadecimal(hex_color) or len(hex_color) != 6:
    raise Exception("not a hex color string")
```

**Option B (alternative grouping):**
```python
if not isinstance(hex_color, str) or not is_hexadecimal(hex_color):
    raise Exception("not a hex color string")
if len(hex_color) != 6:
    raise Exception("not a hex color string")
```

Both approaches work because they ensure `len()` is never called on non-string types.

### Exception Types vs Error Messages

**Important distinction:**
- `len(1000000)` **does raise an exception** (TypeError)
- But it raises `"object of type 'int' has no len()"`
- Our tests expect `"not a hex color string"`
- **Wrong exception message = test failure**

**The two-stage approach ensures:**
1. ✅ No TypeError crashes
2. ✅ Consistent exception message
3. ✅ All test cases pass with expected error messages

### Key Takeaway for Debugging

**When validating input that could be different types:**
1. **Check type first** - ensure safe operations
2. **Then validate content** - only after type is confirmed
3. **Maintain consistent error messages** - match expected test output

This pattern applies broadly in software development: always validate that operations are safe to perform before performing them.