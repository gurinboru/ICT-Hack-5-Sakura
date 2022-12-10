from django.contrib import admin
from .models import Organization,StatusProject, StatusApproval,Student,Project,StudentProject,Rialto,ApprovalPermission
#
# admin.site.register(Organization)
# admin.site.register(Student)

admin.site.register(StudentProject)
admin.site.register(Rialto)
admin.site.register(ApprovalPermission)
admin.site.register(StatusApproval)
admin.site.register(StatusProject)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'INN')
admin.site.register(Organization, OrganizationAdmin)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'definitions', 'budjet','dedlines','positions','techDocument','goalOfProject','background','result','criterias','tags','id_status','status_approval','organization','contactPerson')
    list_filter = ['status_approval']

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.type == 'status_approval':
            return ['name', 'definitions', 'budjet','dedlines','positions','techDocument','goalOfProject','background','result','criterias','tags','id_status','status_approval','organization','contactPerson']
        # return ['name', 'definitions', 'budjet','dedlines','positions','techDocument','goalOfProject','background','result','criterias','tags','id_status','status_approval','organization','contactPerson']

admin.site.register(Project,ProjectAdmin)