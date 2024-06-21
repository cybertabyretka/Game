from BaseVariables.Saves.Saves import AUTO_SAVES, SAVES


def delete_all_saves():
    for save in [*AUTO_SAVES, *SAVES]:
        save.delete()