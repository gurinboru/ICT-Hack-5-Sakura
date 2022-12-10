from django.contrib import admin
from .models import Organization,StatusProject, StatusApproval,Student,Project,StudentProject,Rialto,ApprovalPermission
#
# admin.site.register(Organization)
# admin.site.register(Student)

admin.site.register(StudentProject)
admin.site.register(Rialto)
admin.site.register(ApprovalPermission)

class StatusApprovalAdmin(admin.ModelAdmin):
    model = StatusApproval
    list_display = ('status',)

admin.site.register(StatusApproval,StatusApprovalAdmin)

class StatusProjectAdmin(admin.ModelAdmin):
    model = StatusProject
    list_display = ('status',)

admin.site.register(StatusProject, StatusProjectAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'INN')
admin.site.register(Organization, OrganizationAdmin)

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'definitions', 'budjet','dedlines','positions','techDocument','goalOfProject','background','result','criterias','tags','id_status','status_approval','organization','contactPerson')
    list_filter = ['status_approval']

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status_approval == StatusApproval.ToBeAgreed:
            return ['name', 'definitions', 'budjet','dedlines','positions','techDocument','goalOfProject','background','result','criterias','tags','id_status','status_approval','organization','contactPerson']
        # return ['name', 'definitions', 'budjet','dedlines','positions','techDocument','goalOfProject','background','result','criterias','tags','id_status','status_approval','organization','contactPerson']

admin.site.register(Project,ProjectAdmin)