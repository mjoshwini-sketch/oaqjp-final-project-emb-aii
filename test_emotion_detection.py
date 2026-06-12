from emotion_detection import emotion_detector

result = emotion_detector("I am happy")

if result["dominant_emotion"] == "joy":
    print("Unit test passed")
else:
    print("Unit test failed")
