import random

captions = [
    "Discover something amazing about {} today! 🚀",
    "You won’t believe how awesome {} can be! 🔥",
    "Level up your day with {} 😎",
    "Exploring the world of {} one step at a time 🌍",
    "Let’s talk about {} today! ✨",
    "{} is taking things to the next level! 💡",
    "Everyone is talking about {} right now 👀"
]

hashtags = [
    "#Trending",
    "#ContentCreator",
    "#DailyPost",
    "#SocialMedia",
    "#Inspiration",
    "#Vibes",
    "#CreativeLife"
]

def generate_post(topic, platform, tone):

    captions_generated = []

    for i in range(3):
        caption = random.choice(captions).format(topic)
        selected_tags = " ".join(random.sample(hashtags, 5))

        post = f"""
Caption {i+1}:
{caption}

Hashtags:
{selected_tags}
"""
        captions_generated.append(post)

    return "\n".join(captions_generated)