# Credit: https://github.com/Gladiator07/JARVIS.git
import wolframalpha
try:
    import speak as spfc
except:
    import core.speak as spfc
try:
    from config import config
except:
    from ..config import config

app_id = config.wolframalpha_id


def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        spfc.speak(
            "Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
