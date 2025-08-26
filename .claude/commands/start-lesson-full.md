# Functional Programming Lesson Starter

## Command: Start New Lesson

```
Please start the next functional programming lesson. Follow these steps:

1. **Assess Current Progress**
   - Read CLAUDE.md to understand completed chapters and lessons
   - Identify current position in learning sequence
   - Determine next lesson to tackle

2. **Update Learning Memory**
   - Use Neo4j memory to record recent lesson completions
   - Update `Programming_Skills` entity with new functional concepts
   - Add key achievements to knowledge graph
   - Track chapter progression (CH2: Complete, CH3: Complete, CH4: In Progress)

3. **Lesson Content Analysis**
   - Read the lesson's Lesson.md file completely
   - Identify core concepts being taught
   - Extract Vietnamese translations and explanations
   - Note practical applications and business use cases

4. **Implementation Assessment**
   - Examine main.py structure and current implementation
   - Analyze main_test.py for test cases and requirements
   - Identify TODO sections and missing functionality
   - Understand testing workflow (run_cases vs submit_cases)

5. **Educational Context & Learning Setup**
   - Provide brief insight connecting to previously mastered concepts
   - Explain how this lesson builds on prior knowledge
   - Share 2-3 key educational points in insight format
   - Set learning expectations and success criteria

6. **Begin Implementation**
   - Start with basic test cases understanding
   - Implement core functionality step by step
   - Use iterative development with testing at each step
   - Apply pure function principles and immutability patterns
```

## Quick Start Templates

### 🎯 **Current Lesson (CH4-L1 Recursion)**
```
Start lesson: Working on CH4-L1 Recursion - factorial_r function.
Steps:
1. Review recursion concepts from lesson content
2. Update Neo4j: "Learning recursion fundamentals in functional programming"
3. Implement factorial_r with base case (n==0 returns 1) and recursive case
4. Test with run_cases first, then submit_cases
5. Apply pure function principles (no side effects, deterministic)
6. Connect to prior reduce/accumulator pattern knowledge
```

### 📈 **Next Lesson Discovery**
```
Find next lesson: Discover what comes after current lesson.
Steps:
1. Check lesson sequence in current chapter
2. If chapter complete, move to next chapter
3. Read next lesson content and requirements
4. Update learning objectives in memory
5. Prepare implementation strategy
```

### 🔄 **Lesson Review & Practice**
```
Review lesson: Reinforce concepts from recently completed lesson.
Steps:
1. Re-read lesson educational content
2. Identify key patterns and principles learned
3. Update CLAUDE.md with new concept mastery
4. Practice implementation variations
5. Connect concepts to real-world applications
```

## Learning Progress Tracking

### 📊 **Chapter Status**
- **Chapter 1**: Fundamentals (Basic exercises 01, 02, 04, 05, 07) ✅
- **Chapter 2**: First-Class Functions (L1-L11 complete) ✅
  - Functions as Values, Lambda, Higher-Order, Map/Filter/Reduce
  - Advanced composition, zip, real-world applications
- **Chapter 3**: Pure Functions (L1-L16 complete) ✅
  - Immutability, memoization, referential transparency
  - I/O containment, debugging, date processing
- **Chapter 4**: Recursion (L1 in progress) 🔄
  - Factorial implementation, base cases, recursive thinking

### 🎓 **Mastery Achievements**
- Perfect test scores across all completed lessons
- Bilingual learning (Vietnamese + English technical concepts)
- Real-world application integration
- Performance optimization techniques
- Advanced debugging and error resolution

### 🚀 **Next Learning Goals**
- Recursive problem-solving patterns
- Advanced recursion techniques
- Functional data structure traversal
- Recursive optimization strategies

## Implementation Workflow

### 🔧 **Standard Approach**
1. **Read & Understand**: Complete lesson analysis
2. **Plan & Design**: Identify core algorithm and approach
3. **Implement & Test**: Iterative development with run_cases
4. **Refine & Perfect**: Full submit_cases testing
5. **Learn & Reflect**: Extract insights and update knowledge

### 🧪 **Testing Strategy**
```bash
# Basic development testing
python -c "__RUN__ = True; exec(open('main_test.py').read())"

# Full test suite validation
python main_test.py
```

### 📝 **Code Quality Standards**
- Pure functions (deterministic, no side effects)
- Input immutability preservation
- Clean, readable implementations
- Proper error handling and edge cases
- Performance-conscious design

## Memory Update Protocol

### 📚 **Learning Achievements**
```
Update Neo4j: Completed $LESSON_NAME with $KEY_CONCEPTS mastery.
Steps:
1. Check Programming_Skills current observations
2. Add new functional programming concept
3. Update chapter completion status
4. Record test score achievements (e.g., "6/6 tests passed")
5. Connect to previous learning foundations
```

### 🎯 **Skill Progression**
```
Update Neo4j: Advanced to $CHAPTER_NAME level in functional programming.
Steps:
1. Update skill level in Programming_Skills
2. Add practical application examples
3. Record bilingual learning achievements
4. Update learning velocity and momentum
5. Set goals for next chapter
```

## Lesson Types & Approaches

### 🔄 **Concept Introduction**
- Focus on understanding theoretical foundations
- Implement basic patterns and examples
- Connect to previously learned concepts
- Build conceptual mental models

### 🛠️ **Practice & Application**
- Apply concepts to real-world scenarios
- Debug and fix implementation issues
- Optimize performance and code quality
- Integrate multiple functional concepts

### 🏆 **Mastery & Integration**
- Combine multiple advanced concepts
- Solve complex, multi-step problems
- Demonstrate expert-level implementation
- Prepare for next learning phase

## Success Metrics

### ✅ **Lesson Completion Criteria**
- All test cases passing (submit_cases)
- Input immutability preserved
- Pure function principles applied
- Code quality meets standards
- Concepts thoroughly understood

### 🎯 **Learning Effectiveness**
- Can explain concepts in both English and Vietnamese
- Able to connect to previous lessons
- Can apply patterns to new problems
- Knowledge retained and accessible

---

**Remember**: Each lesson builds on previous foundations. Master each concept thoroughly before advancing! 🚀
