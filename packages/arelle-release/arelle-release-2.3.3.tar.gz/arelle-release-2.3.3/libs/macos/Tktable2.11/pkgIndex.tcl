if {[catch {package require Tcl 8.2}]} return
package ifneeded Tktable 2.11     [list load [file join $dir libTktable2.11.dylib] Tktable]
