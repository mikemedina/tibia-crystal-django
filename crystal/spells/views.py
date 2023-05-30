from django.http import JsonResponse

from .models import Spell


def get_spells_by_vocation(request):
    level = request.GET.get('level')
    magic_level = request.GET.get('magic_level')
    vocation = request.GET.get('vocation').lower()
    if vocation in ['ed', 'druid', 'elder druid']:
        vocation = 'druid'
    elif vocation in ['ek', 'knight', 'elite knight']:
        vocation = 'knight'
    elif vocation in ['ms', 'sorc', 'sorcerer', 'master sorc',
                      'master sorcerer']:
        vocation = 'sorcerer'
    elif vocation in ['rp', 'pally', 'paladin', 'royal paladin']:
        vocation = 'paladin'
    else:
        # Invalid vocation provided
        return JsonResponse({'error': 'Invalid vocation'}, status=400)

    # Query spells with matching vocation column
    spells = Spell.objects.filter(vocation=vocation)

    # Create a list of dictionaries representing each spell
    spells_list = []
    for spell in spells:
        spell_dict = {
            'name': spell.name,
            'vocation': spell.vocation,
            'x_max': spell.x_max,
            'y_max': spell.y_max,
            'x_min': spell.x_min,
            'y_min': spell.y_min,
            'target_cap': spell.target_cap
        }
        spells_list.append(spell_dict)

    return JsonResponse(spells_list, safe=False)
