from tasks_api.core.enum.statusenum import StatusEnum

class ResponseWrapper():
    def responseModel(self, data):
        response = list(map(self.__createResponseItem, data))
        return response

    def __createResponseItem(self, workspaceItem):
        self.tasks_not_started = self.__taskCountByStatus(workspaceItem['tasks'], StatusEnum.NOT_STARTED.value)
        self.tasks_in_progress = self.__taskCountByStatus(workspaceItem['tasks'], StatusEnum.IN_PROGRESS.value)
        self.tasks_completed = self.__taskCountByStatus(workspaceItem['tasks'], StatusEnum.COMPLETED.value)
        self.progress = self.__calculate_progress(self.tasks_in_progress, self.tasks_completed, workspaceItem['total_task_count'])
        
        return {
           'id': workspaceItem['id'],
           'name': workspaceItem['name'],
           'total_task_count': workspaceItem['total_task_count'],
           'bgcolor': workspaceItem['bgcolor'], 
           'created_at': workspaceItem['created_at'],
           'updated_at': workspaceItem['updated_at'],
           'not_started_task_count': len(self.tasks_not_started),
           'in_progress_task_count': len(self.tasks_in_progress),
           'completed_task_count': len(self.tasks_completed),
           'progress': self.progress
        }

    def __taskCountByStatus(self, task_list, status):
        return list(filter(lambda x: x['status'] == status, task_list))

    def __calculate_progress(self, in_progress, completed, total):
        if total != 0:
            self.completed_percentage = len(completed) / total

            if len(in_progress) == 0:
                self.in_progress_percentage = 0
            else:
                self.in_progress_percentage = len(completed) / len(in_progress)

            return round((self.completed_percentage + self.in_progress_percentage) * 100)
        else :
            return 0

        