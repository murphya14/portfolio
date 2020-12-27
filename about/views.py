#!/usr/bin/python
# -*- coding: utf-8 -*-
from hobby_product.models import hobby_product
from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def about_surf(request):
    """ Return about page """
    #return redirect(reverse('home'))
    return render(request, 'about.html')

