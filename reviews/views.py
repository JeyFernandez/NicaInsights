from django.shortcuts import render

# Create your views here.
def home(request):
    lugares = [
        'Granada',
        'León',
        'Matagalpa',
        'Estelí',
        'Rivas',
        'San Juan del Sur',
        'Isla de Ometepe',
        'Corn Island',
        'Managua',
        'Masaya',
        'San Juan del Sur',
        'San Juan del Sur',
        'San Juan del Sur',
    ]
    return render(request, 'home.html', {'lugares': lugares})