# Functional vs. OOP

Functional programming and object-oriented programming are **styles for writing code**. One isn't inherently superior to the other, but to be a well-rounded developer you should understand both well and use ideas from each when appropriate.

You'll encounter developers who love functional programming and others who love object-oriented programming. However, contrary to popular opinion, FP and OOP are *not* always at odds with one another. They aren't opposites. Of the four pillars of OOP, [inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)) is the only one that doesn't fit with functional programming.

![FP vs OOP Comparison](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/8ZrwpU2-831x500.png)

Inheritance isn't seen in functional code due to the mutable classes that come along with it. Encapsulation, polymorphism and abstraction are still used all the time in functional programming.

When working in a language that supports ideas from both FP and OOP (like Python, JavaScript, or Go) the best developers are the ones who can use the best ideas from both paradigms effectively and appropriately.

## Key Takeaways

### The Four Pillars of OOP
1. **Encapsulation** ✅ Compatible with FP
2. **Polymorphism** ✅ Compatible with FP  
3. **Abstraction** ✅ Compatible with FP
4. **Inheritance** ❌ Not compatible with FP (due to mutability)

### Best Practice
- Use FP principles for data transformation and pure logic
- Use OOP principles for modeling complex systems and state management
- Combine both approaches where appropriate in multi-paradigm languages

---

## Detailed Explanation

### What Are Programming Paradigms?

Programming paradigms are **different philosophies for organizing and structuring code**. Think of them like architectural styles for buildings - you could build the same house using modern, classical, or minimalist approaches. Each style has strengths for different situations.

### Functional Programming (FP) Philosophy

**Core principle**: "Computation is the evaluation of mathematical functions"

**Key characteristics:**
- **Immutable data**: Once created, data never changes
- **Pure functions**: Same input always produces same output, no side effects
- **Function composition**: Build complex operations by combining simple functions
- **No hidden state**: Everything needed is passed as parameters

**Example in AI development:**
```python
# FP approach to text processing
def clean_text(text):
    return text.strip().lower()

def extract_keywords(text): 
    return text.split()

def process_document(doc):
    cleaned = clean_text(doc)
    keywords = extract_keywords(cleaned)
    return keywords
```

### Object-Oriented Programming (OOP) Philosophy

**Core principle**: "Computation is interaction between objects that contain both data and behavior"

### The Four Pillars of OOP Explained

#### 1. **Encapsulation** ✅ Compatible with FP
- **What**: Bundle data and methods that operate on that data together
- **Why**: Hide internal complexity, control access
- **Example**: AI agent class hides complex model API calls behind simple methods

```python
class ContractAgent:
    def __init__(self, model_api):
        self._model = model_api  # Hidden internal state
        self._context = []
    
    def analyze_contract(self, text):  # Public interface
        return self._model.process(text)  # Internal complexity hidden
```

**FP Compatible Version:**
```python
# Functional encapsulation - module with related functions
def create_agent_config(model, temperature):
    return {"model": model, "temp": temperature}

def process_with_config(config, text):
    # All data passed explicitly, no hidden mutable state
    return model_api.call(config, text)
```

#### 2. **Abstraction** ✅ Compatible with FP
- **What**: Hide implementation details, show only essential features
- **Why**: Reduces complexity, allows focusing on high-level concepts
- **Example**: You don't need to know how Claude's API works internally, just how to call it

**FP Compatible Version:**
```python
# Abstract away complexity with function composition
def ai_pipeline(text):
    return analyze(extract(clean(text)))  # High-level abstraction
```

#### 3. **Polymorphism** ✅ Compatible with FP
- **What**: Different objects can respond to the same interface differently
- **Why**: Write code that works with multiple types
- **Example**: Different AI models (GPT, Claude, Gemini) all implement a `generate_response()` method

```python
# OOP polymorphism
gpt_agent.generate_response(prompt)
claude_agent.generate_response(prompt)  
gemini_agent.generate_response(prompt)
```

**FP Compatible Version:**
```python
# Functional polymorphism
def process_with_gpt(text): return gpt_api(text)
def process_with_claude(text): return claude_api(text)

# Use polymorphically
models = [process_with_gpt, process_with_claude]
for model in models:
    result = model(text)  # Same interface
```

#### 4. **Inheritance** ❌ Not Compatible with FP
- **What**: New classes inherit properties and methods from existing classes
- **Why**: Code reuse, hierarchical relationships
- **Problem**: Typically involves mutable shared state

```python
# This violates FP principles
class Agent:
    def __init__(self):
        self.state = []  # Mutable state!
    
    def process(self, data):
        self.state.append(data)  # Side effect! Modifies state!

class SpecialAgent(Agent):  # Inheritance carries mutable state
    def special_process(self, data):
        self.state.append(f"special: {data}")  # More mutation!
```

**Why inheritance conflicts**: It typically involves mutable shared state between parent and child classes, violating FP's immutability principle.

### Practical Hybrid Approach: Multi-Agent Systems

**Best of both worlds** - OOP structure with FP data flow:

```python
# OOP structure for system organization
class AgentOrchestrator:
    def __init__(self, agents):
        self._agents = agents  # Encapsulation
    
    def process_request(self, request):
        # FP pipeline inside OOP structure
        return self._compose_responses(
            self._gather_agent_responses(request)
        )
    
    # Pure functional methods inside OOP class
    def _gather_agent_responses(self, request):
        return [agent.respond(request) for agent in self._agents]
    
    def _compose_responses(self, responses):
        return {"combined": responses, "confidence": self._calculate_confidence(responses)}
```

This gives you:
- **OOP benefits**: Clear system structure, encapsulated complexity
- **FP benefits**: Predictable data flow, easy testing, no hidden mutations

### Final Key Points

1. **FP and OOP are complementary**, not opposing paradigms
2. **Only inheritance conflicts with FP** - the other three pillars work fine
3. **Use hybrid approaches** in multi-paradigm languages like Python
4. **Choose the right tool**: FP for data transformation, OOP for system structure
5. **Be pragmatic, not dogmatic** - use what works best for your specific problem