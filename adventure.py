"""Choose Your Own Adventure Stories."""

class AdventureStory:
    """Adventure story for a choose-your-own-path experience.

    To create a story, pass a list of choices and the template
    text for each choice outcome.

        >>> s = AdventureStory(["left", "right"],
        ...     {
        ...         "left": "You went left and found a treasure!",
        ...         "right": "You went right and fell into a pit!"
        ...     })

    To generate text from a story, pass in the choice made by the user:

        >>> choice = "left"
        >>> s.generate(choice)
        'You went left and found a treasure!'
    """

    def __init__(self, choices, outcomes):
        """Create story with choices and outcomes."""

        self.choices = choices
        self.outcomes = outcomes

    def generate(self, choice):
        """Return outcome based on choice."""

        return self.outcomes[choice]

# Here's a story to get you started

adventure_story = AdventureStory(
    ["left", "right"],
    {
        "left": "Once upon a time, you took the left path and discovered a hidden waterfall.",
        "right": "Venturing right led you to an ancient castle shrouded in mist."
    }
)
