# Reddit2Podcast

Transforms a Reddit discussion thread into a Podcast transcript.

### Usage

```shell
$ make run url=https://old.reddit.com/r/Awww/comments/1e9ecvq/this_is_an_uninterrupted_minute_of_maruay_the/
```

Converts [this thread](https://old.reddit.com/r/Awww/comments/1e9ecvq/this_is_an_uninterrupted_minute_of_maruay_the/) into:

```json
[
  {
    "speaker": "Anna",
    "dialogue": "Hey Elsa I heard about this adorable tiger Maruay who loves a big red ball"
  },
  {
    "speaker": "Elsa",
    "dialogue": "[laugh] yeah I saw it too isn't it sweet that he's so attached to the ball"
  },
  {
    "speaker": "Anna",
    "dialogue": "I know right it's like he can't get enough of it and just holds it close with such joy on his face"
  },
  {
    "speaker": "Elsa",
    "dialogue": "And people were commenting about how it might be fragile or that Maruay is using it as a flotation device in the water"
  },
  {
    "speaker": "Anna",
    "dialogue": "[laugh] yeah I saw those comments and I was like ahaha isn't it funny how we all have our own things that bring us such happiness"
  },
  {
    "speaker": "Elsa",
    "dialogue": "Exactly and some people were even drawing parallels between Maruay's love for the ball and human emotional connections which is really interesting"
  },
  {
    "speaker": "Anna",
    "dialogue": "[uv_break] and I loved how people started speculating about what the ball might be made of or if it's durable"
  },
  {
    "speaker": "Elsa",
    "dialogue": "Yeah me too and then someone mentioned Tom Hanks' love of a football in Cast Away which was like oh yeah that makes sense"
  },
  {
    "speaker": "Anna",
    "dialogue": "[laugh] right it's like we all have our own little things that bring us comfort and security"
  },
  {
    "speaker": "Elsa",
    "dialogue": "Exactly and I think that's what made this whole thing so endearing to people is the simple pleasure of a tiger loving his red ball"
  },
  {
    "speaker": "Anna",
    "dialogue": "[uv_break] I don't know about you but now I'm craving something similar just to relax and enjoy life like Maruay with his ball"
  },
  {
    "speaker": "Elsa",
    "dialogue": "[laugh] me too let's go find our own red balls or whatever brings us joy"
  }
]
```


### Progress

- [x] Fetch Reddit comments
- [x] Parse comments
- [x] Generate summary
- [x] Generate transcript
- [ ] Convert to audio




### License

MIT