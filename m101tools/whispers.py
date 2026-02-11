from datetime import datetime as dt 

def simulator(audio_path: str) -> dict:
    """Simulate transcription for testing"""
    print(f"[SIMULATED] Processing: {audio_path}")
    
    return {
        "text": "هذا نص تجريبي باللغة العربية",
        "confidence": 0.95,
        "duration": 5.0,
        "language": "ar"
    }

def format_ts(seconds: float) -> str: 
    """Format timestamps

    Requires: 
    Returns: 
    """
    if seconds is None: 
        return "00:00:00.000" 

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"
