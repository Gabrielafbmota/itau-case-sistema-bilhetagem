class GetUserByIdUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id):
        return self.user_repository.get_user_by_id(user_id)
