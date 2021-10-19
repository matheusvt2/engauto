from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms.script_form import RunForm, RawRunForm


@login_required()
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RunForm(request.POST)
        # get user and pass from post (not in History model)
        # server_user = request.POST["server_user"]
        # server_pass = request.POST["server_pass"]
        # server = request.POST["server"]
        # script = request.POST["script"]
        # check whether it's valid:
        if form.is_valid():
            form = form.save(commit=False)
            # insert values for hidden fields
            # form.exectime = datetime.now()
            # terminal_output =  subprocess.run(['python3',f'remediacao/scripts/{script}',server,server_user,server_pass], capture_output=True, text=True)
            # form.terminal = terminal_output.stdout 
            # form.terminal_error = terminal_output.stderr 
            # form.returncode = terminal_output.returncode
            # form.job = "Remediação"
            form.save()
            return HttpResponseRedirect('/api/history')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RawRunForm()
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', {'form': form})
    
