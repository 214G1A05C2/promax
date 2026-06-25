# Clinic Metrics Backend

## API

### `GET /api/call-metrics`
Returns all call metrics in a clean, predictable envelope:

```json
{
  "success": true,
  "count": 1,
  "data": [
    {
      "id": "8fea7ce0-e6b9-4f66-8409-48576eda2097",
      "call_id": 123,
      "clinic_name": "Test Clinic",
      "call_timestamp": "2026-06-11 10:00:00",
      "primary_intent": "test",
      "secondary_intents": [],
      "detected_intents": {},
      "workflow_events": [],
      "workflow_summary": {},
      "completion_data": {},
      "blocker_data": {},
      "final_output": null,
      "created_at": null,
      "transcript": null
    }
  ]
}
```

### `GET /api/call-metrics/<call_id>`
Returns one record by `call_id`.

### `POST /api/call-metrics`
Accepts plain JSON objects and arrays for the nested fields. If you send a JSON string, it will be stored as-is. If you send a list or object, it is saved correctly as JSON text.

Example payload:

```json
{
  "call_id": 123,
  "clinic_name": "Test Clinic",
  "call_timestamp": "2026-06-11 10:00:00",
  "primary_intent": "test",
  "secondary_intents": ["billing", "follow_up"],
  "detected_intents": {
    "primary_intent": "test"
  },
  "workflow_events": [],
  "workflow_summary": {
    "current_workflow_state": "COMPLETED"
  },
  "completion_data": {
    "primary_intent_completed": true
  },
  "blocker_data": {
    "last_unresolved_blocker": null
  },
  "final_output": "Call completed successfully",
  "created_at": "2026-06-20 11:45:11",
  "transcript": []
}
```

### `DELETE /api/call-metrics/<call_id>`
Deletes the first record that matches the numeric `call_id`.

## Notes

- JSON-like columns are normalized on output, so the response is easy to read.
- The database schema uses text columns for nested data, so the backend converts lists/objects to JSON strings on save and back to native JSON on read.
