from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_hint_messages():
    # Test that the hint messages are correct for each outcome
    
    # Win casebb
    outcome, message = check_guess(75, 75)
    assert outcome == "Win"
    assert message == "🎉 Correct!"
    
    # Too low case
    outcome, message = check_guess(25, 75)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
    
    # Too high case
    outcome, message = check_guess(90, 75)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_hint_messages_edge_cases():
    # Test edge cases to ensure messages are consistent
    
    # Guess just below secret
    outcome, message = check_guess(74, 75)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
    
    # Guess just above secret
    outcome, message = check_guess(76, 75)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"
    
    # Large numbers
    outcome, message = check_guess(100, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"
    
    outcome, message = check_guess(1, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
