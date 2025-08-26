# Neo4j Memory Update Protocol

## Command: Update Neo4j Memory

```
Please update the Neo4j memory with: $ARGUMENTS.
Follow these steps:

1. Use `read_graph` to get current state and verify entity exists
2. Analyze what type of update is needed (add/modify/remove)
3. Search for related entities that might be affected
4. Implement the update using appropriate method:
   - For new info: `add_observations` 
   - For corrections: `delete_observations` then `add_observations`
   - For new connections: `create_relations`
5. Verify no duplicates or conflicts were created
6. Check observation count stays ≤5 per entity
7. Consolidate if any entity becomes bloated
8. Read graph again to confirm successful update

Remember to maintain the 7-entity structure for optimal performance.
```

## Quick Update Templates

### 📚 Learning Update
```
Update Neo4j: Learned $TOPIC from $SOURCE.
Steps:
1. Check `Programming_Skills` current observations
2. If count ≥ 4, remove oldest non-core skill
3. Add new learning as concise observation
4. Update relation to `AI_Development` if relevant
5. Verify workspace path still accurate
```

### 🚀 Project Progress  
```
Update Neo4j: Project $NAME status is $STATUS.
Steps:
1. Check `Active_Projects` for existing entry
2. If completed:
   - Extract key achievement → `AI_Development`
   - Remove from `Active_Projects`
3. If new: Add to `Active_Projects` (max 4 concurrent)
4. Update income relation to `Business_Operations` if applicable
5. Verify total active projects ≤ 4
```

### 💻 Tech Stack Change
```
Update Neo4j: Changed $TOOL to $NEW_TOOL for $REASON.
Steps:
1. Read `System_Setup` observations
2. Find and remove old tool reference
3. Add new tool with context (e.g., "VSCode → Cursor for AI features")
4. Update `Programming_Skills` if affects workflow
5. Check no orphaned dependencies remain
```

### 💰 Business Update
```
Update Neo4j: Business change - $DESCRIPTION.
Steps:
1. Check `Business_Operations` current state
2. Update relevant observation (rent/revenue/costs)
3. If new income source, add relation from `Active_Projects`
4. Keep financial data aggregated, not detailed
5. Archive old contracts/deals after completion
```

### 🏥 Health Status
```
Update Neo4j: Health update - $CONDITION.
Steps:
1. Read `Health_Status` observations
2. Keep only most recent treatment/diagnosis
3. Update routine if changed
4. Maintain equipment list only if actively used
5. Max 4 observations total
```

## Batch Update Protocol

### 🔄 Weekly Maintenance
```
Perform Neo4j weekly maintenance.
Steps:
1. Read full graph
2. For each entity with >4 observations:
   - Identify outdated info
   - Consolidate similar observations
   - Delete redundant data
3. Check for orphaned relations
4. Archive completed projects
5. Update `User` entity if personal info changed
6. Generate summary of changes made
```

### 🎯 Focus Area Shift
```
Update Neo4j: Shifting focus from $OLD_AREA to $NEW_AREA.
Steps:
1. Identify affected entities (usually 2-3)
2. Archive/reduce $OLD_AREA observations
3. Create space for $NEW_AREA content
4. Update relations to reflect new priorities
5. Ensure `Active_Projects` aligns with new focus
6. Keep total entity count at 7
```

## Error Recovery

### 🔧 Fix Duplicate Data
```
Fix Neo4j: Found duplicate - $DESCRIPTION.
Steps:
1. Search both entities/observations
2. Identify which has more recent data
3. Merge unique info from both
4. Delete duplicate entity/observation
5. Update relations to point to merged entity
6. Verify graph integrity
```

### 🗑️ Clean Obsolete Data
```
Clean Neo4j: Remove obsolete $CATEGORY data.
Steps:
1. Identify observations older than 3 months
2. Check if still relevant/active
3. For obsolete items:
   - Extract any achievements
   - Delete detailed progress
   - Keep only outcomes
4. Reduce each entity to ≤4 observations
5. Verify essential info preserved
```

## Validation Checklist

After any update, verify:
- [ ] Total entities = 7 (no more, no less)
- [ ] Each entity has ≤5 observations
- [ ] No duplicate information across entities
- [ ] Relations make semantic sense
- [ ] User entity has core info only
- [ ] Active projects ≤ 4
- [ ] Technical domains are current
- [ ] Business data is aggregated

## Example Usage

```bash
# Learning update
"Update Neo4j: Learned Advanced Prompting from Anthropic docs."

# Project completion  
"Update Neo4j: GAIA Solver project completed with 85% accuracy."

# System change
"Update Neo4j: Switched from i3wm to Hyprland for better animations."

# Health improvement
"Update Neo4j: Back pain improved, stopped medication, continuing exercises."

# Business milestone
"Update Neo4j: Rental income increased to 70M/month starting January."
```

## Performance Metrics

Target after update:
- Query time: <100ms
- Memory usage: <1MB
- Observations total: <30
- Relations total: <10
- Update time: <2s

---

**Remember**: Every update should make the graph leaner and more current! 🚀
