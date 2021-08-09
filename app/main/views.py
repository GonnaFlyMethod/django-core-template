from django.shortcuts import render


class SignUpView(View):

	def get(self, request):
		return render(request, 'main/main_page.html')
