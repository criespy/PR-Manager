from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PRDocumentForm, PRDocumentDetailFormSet

#@login_required
def create_pr_document(request):
    if request.method == 'POST':
        # Membuat form untuk PR_Document
        pr_form = PRDocumentForm(request.POST)
        # Membuat formset untuk PR_Document_Detail
        detail_formset = PRDocumentDetailFormSet(request.POST)

        if pr_form.is_valid() and detail_formset.is_valid():
            # Simpan PR_Document
            pr_document = pr_form.save(commit=False)
            pr_document.created_by = request.user  # Set created_by ke user yang sedang login
            pr_document.save()

            # Simpan PR_Document_Detail
            details = detail_formset.save(commit=False)
            for detail in details:
                detail.pr_document = pr_document  # Hubungkan detail dengan PR_Document
                detail.save()

            return redirect('success_page')  # Redirect ke halaman sukses
    else:
        pr_form = PRDocumentForm()
        detail_formset = PRDocumentDetailFormSet()

    return render(request, 'create_pr_document.html', {
        'pr_form': pr_form,
        'detail_formset': detail_formset,
    })