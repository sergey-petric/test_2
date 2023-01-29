def create_handlers(callback) -> list:
    handlers: list = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda i=step: callback(step))
    return handlers


def execute_handlers(handlers: list) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()
