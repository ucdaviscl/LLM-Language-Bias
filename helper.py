from statistics import mean

def score_mfq(responses):
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
    
    return {
        'Harm': harm_avg,
        'Fairness': fairness_avg,
        'Ingroup': ingroup_avg,
        'Authority': authority_avg,
        'Purity': purity_avg,
        'Overall': overall_avg
    }