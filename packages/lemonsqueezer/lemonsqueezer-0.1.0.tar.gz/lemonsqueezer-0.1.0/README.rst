LemonSqueezer
=============

* Kill subprocesses on exit - 
    - Fixed reading non-existent config file, but it hangs on because the button handler
      waits for the bar's stdout. IDEA: add read and write locks?

* Allow using config colors in modules
    - IDEA: provide dummy values from the bar, representing each colour. When the module
      sees them, it asks the bar for the appropriate color

DONE
====

* Refresh BSPWM modules on more events 
