def strategy(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    # Initial move: cooperate
    if not opponent_history:
        return 1
    
    # Strategic final move if total rounds are known
    if rounds is not None and len(my_history) == rounds - 1:
        return 0
    
    # Analyze opponent's behavior in last 5 moves
    lookback = 5
    recent_moves = opponent_history[-lookback:] if opponent_history else []
    if recent_moves:
        defects = len(recent_moves) - sum(recent_moves)
        # Defect if >40% defects in recent history
        if defects / len(recent_moves) > 0.4:
            return 0
    
    # Default to Tit-for-Tat with forgiveness
    if opponent_history[-1] == 0:
        # Check if opponent has cooperated in 2/3 of previous 3 moves
        if len(opponent_history) >= 3 and sum(opponent_history[-3:]) >= 2:
            return 1  # Forgive occasional defects
        return 0
    return 1