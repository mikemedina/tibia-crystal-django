from django.db import migrations


def populate_spells(apps, schema_editor):
    Spell = apps.get_model('spells', 'Spell')
    spells_data = [
        {
            'name': 'Avalanche',
            'vocation': 'druid',
            'x_max': 2.85,
            'y_max': 16,
            'x_min': 1.2,
            'y_min': 7,
            'target_cap': 11
        },
        {
            'name': 'Energy Strike',
            'vocation': 'druid',
            'x_max': 2.203,
            'y_max': 14,
            'x_min': 1.403,
            'y_min': 8,
            'target_cap': 1
        },
        {
            'name': 'Eternal Winter',
            'vocation': 'druid',
            'x_max': 11,
            'y_max': 50,
            'x_min': 5.5,
            'y_min': 25,
            'target_cap': 16
        },
        {
            'name': 'Explosion',
            'vocation': 'druid',
            'x_max': 3.2,
            'y_max': 19,
            'x_min': 1.6,
            'y_min': 9,
            'target_cap': 4
        },
        {
            'name': 'Fireball',
            'vocation': 'druid',
            'x_max': 3,
            'y_max': 17,
            'x_min': 1.81,
            'y_min': 12,
            'target_cap': 1
        },
        {
            'name': 'Heal Friend',
            'vocation': 'druid',
            'x_max': 14.4,
            'y_max': 90,
            'x_min': 6.3,
            'y_min': 45,
            'target_cap': 1
        },
        {
            'name': 'Heavy Magic Missile',
            'vocation': 'druid',
            'x_max': 1.59,
            'y_max': 10,
            'x_min': 0.81,
            'y_min': 5,
            'target_cap': 1
        },
        {
            'name': 'Ice Wave',
            'vocation': 'druid',
            'x_max': 2,
            'y_max': 12,
            'x_min': 0.81,
            'y_min': 5,
            'target_cap': 9
        },
        {
            'name': 'Intense Healing',
            'vocation': 'druid',
            'x_max': 6,
            'y_max': 37,
            'x_min': 3.6,
            'y_min': 22,
            'target_cap': 1
        },
        {
            'name': 'Light Healing',
            'vocation': 'druid',
            'x_max': 1.8,
            'y_max': 11,
            'x_min': 1.4,
            'y_min': 8,
            'target_cap': 1
        },
        {
            'name': 'Light Magic Missile',
            'vocation': 'druid',
            'x_max': 0.81,
            'y_max': 4,
            'x_min': 0.4,
            'y_min': 3,
            'target_cap': 1
        },
        {
            'name': 'Mass Healing',
            'vocation': 'druid',
            'x_max': 9.6,
            'y_max': 125,
            'x_min': 4.6,
            'y_min': 100,
            'target_cap': 1
        },
        {
            'name': 'Physical Strike',
            'vocation': 'druid',
            'x_max': 2.203,
            'y_max': 14,
            'x_min': 1.403,
            'y_min': 8,
            'target_cap': 1
        },
        {
            'name': 'Stalagmite',
            'vocation': 'druid',
            'x_max': 1.59,
            'y_max': 10,
            'x_min': 0.81,
            'y_min': 5,
            'target_cap': 1
        },
        {
            'name': 'Stone Shower',
            'vocation': 'druid',
            'x_max': 2.6,
            'y_max': 16,
            'x_min': 1,
            'y_min': 6,
            'target_cap': 1
        },
        {
            'name': 'Strong Ice Strike',
            'vocation': 'druid',
            'x_max': 4.4,
            'y_max': 28,
            'x_min': 2.8,
            'y_min': 16,
            'target_cap': 1
        },
        {
            'name': 'Strong Ice Wave',
            'vocation': 'druid',
            'x_max': 7.6,
            'y_max': 48,
            'x_min': 4.5,
            'y_min': 20,
            'target_cap': 6
        },
        {
            'name': 'Sudden Death',
            'vocation': 'druid',
            'x_max': 7.4,
            'y_max': 48,
            'x_min': 4.3,
            'y_min': 32,
            'target_cap': 1
        },
        {
            'name': 'Terra Wave',
            'vocation': 'druid',
            'x_max': 6.75,
            'y_max': 30,
            'x_min': 3.25,
            'y_min': 5,
            'target_cap': 8
        },
        {
            'name': 'Ultimate Healing',
            'vocation': 'druid',
            'x_max': 12.9,
            'y_max': 90,
            'x_min': 6.8,
            'y_min': 42,
            'target_cap': 1
        },
        {
            'name': 'Ultimate Ice Strike',
            'vocation': 'druid',
            'x_max': 7.3,
            'y_max': 55,
            'x_min': 4.5,
            'y_min': 35,
            'target_cap': 1
        },
        {
            'name': 'Wrath of Nature',
            'vocation': 'druid',
            'x_max': 9,
            'y_max': 40,
            'x_min': 3,
            'y_min': 32,
            'target_cap': 20
        }
    ]

    for spell_data in spells_data:
        Spell.objects.create(**spell_data)


class Migration(migrations.Migration):
    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_spells),
    ]
