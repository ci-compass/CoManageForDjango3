from django.shortcuts import render

from .models import IsMemberOf, LdapOther


def ldap_attributes(request):
    user = request.user
    if user.is_authenticated:
        user_id = user.id
    else:
        user_id = 0
    ismemberof = IsMemberOf.objects.filter(membershipismemberof__user_id=user_id).order_by('value')
    ldapother = LdapOther.objects.filter(membershipldapother__user_id=user_id).order_by('attribute', 'value')
    return render(request, 'login.html', {'isMemberOf': ismemberof, 'LDAPOther': ldapother})
