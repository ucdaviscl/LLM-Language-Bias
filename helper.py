import openai
from statistics import mean

def query_gpt3_5_turbo(prompt, max_tokens=1000, language="english"):
    system_message = {
        "english": "You are a helpful assistant.",
        "spanish": "Eres un asistente útil.",
        "mandarin": "你是一个有用的助手。",
    }

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": system_message[language]},
                  {"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )

    return response.choices[0].message['content']

def score_mfq(responses, response_type="dict"):
    harm = [responses[0], responses[6], responses[21], responses[16], responses[27]]
    fairness = [responses[1], responses[7], responses[12], responses[23], responses[17], responses[28]]
    ingroup = [responses[2], responses[8], responses[13], responses[22], responses[18], responses[29]]
    authority = [responses[3], responses[9], responses[24], responses[19], responses[31]]
    purity = [responses[4], responses[10], responses[25], responses[20], responses[26]]

    harm_avg = mean(harm)
    fairness_avg = mean(fairness)
    ingroup_avg = mean(ingroup)
    authority_avg = mean(authority)
    purity_avg = mean(purity)

    overall_avg = mean([harm_avg, fairness_avg, ingroup_avg, authority_avg, purity_avg])
    
    if response_type == "dict":
        return {
            'Harm': harm_avg,
            'Fairness': fairness_avg,
            'Ingroup': ingroup_avg,
            'Authority': authority_avg,
            'Purity': purity_avg,
            'Overall': overall_avg
        }
    elif response_type == "list":
        return [harm_avg, fairness_avg, ingroup_avg, authority_avg, purity_avg, overall_avg]
    else:
        return "Invalid response type. Please use 'dict' or 'list'."