def patient_selected(request):

    print(hasattr(request, 'patient_selected_id'))

    if not hasattr(request, 'patient_selected_id'):
        request.patient_selected_id = 0
    print(request.resolver_match.url_name)
    if(request.resolver_match.url_name == 'patient-detail'):
        print(request.resolver_match.kwargs['pk'])
        request.patient_selected_id = request.resolver_match.kwargs['pk']
        return {
            "patient_selected_id": request.patient_selected_id,
        }
    
    return {"patient_selected_id": 0}
    #