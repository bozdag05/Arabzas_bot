from aiogram.dispatcher.filters.state import StatesGroup, State


class state_1(StatesGroup):
    del_id_state = State()
    word_id_state = State()
    write_state_rus = State()
    write_state_arab = State()
    test_state_arab = State()
    test_state_rus = State()


class my_state(StatesGroup):
    my_word_id_state = State()
    my_write_state_rus = State()
    my_write_state_arab = State()
    my_test_state_arab = State()
    my_test_state_rus = State()


class user_state(StatesGroup):
    add_word_state = State()
    add_translation_state = State()
    get_id_state = State()


class admin_state(StatesGroup):
    add_word_state = State()
    add_translation_state = State()
    get_id_state = State()
    get_level_lesson = State()


class word_state(StatesGroup):
    level_state = State()
    lesson_state = State()
    word_state = State()
    translation_state = State()


class callback(StatesGroup):
    callback_from_admin = State()
    callback_from_user = State()
    callback_text_user = State()
    update_status_user = State()