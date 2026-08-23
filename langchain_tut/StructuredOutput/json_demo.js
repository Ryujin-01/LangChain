demo = {
    "title": "Student Profile",
    "type": "object",
    "description": "A student profile including student details",
    "properties": {
        "name": { 
            "type": "string" 
        },
        "age": { 
            "type": "number" 
        },
        "cgpa": { 
            "type": "number" 
        },
        "email": { 
            "type": "string" 
        }
    },
    "required": [
        "name", 
        "age", 
        "cgpa"
    ]
}