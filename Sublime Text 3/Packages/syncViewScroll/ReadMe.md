# syncViewScroll Package For sublimeText

--------

## About

Sync View Scroll is a simple [Sublime Text 3](http://www.sublimetext.com/3 ) plug-in which allows sync scroll among views.

*note: st2 should work, if you find any bug, please open an issue at github.*

## Install

Using [Package Control](https://sublime.wbond.net/installation) && search `syncviewscroll`

*OR*

Just clone this repo and put it under your sublime-text package folder.

## Usage

1. In one View, goto `View`, check the `Sync Scroll` checkbox. (OR using command palette with 'syncscroll')
2. Repeat step 1 on all other view you want to sync view
3. Scroll on one of these views, the others sync scrolls.
4. You can set `{ "keys": [your_keys_here], "command": "toggle_sync_scroll" }` in user's keymap to trigger sync scroll(thanks to [@KaduAmaral](https://github.com/KaduAmaral))

## Author
zzjin tczzjin#gmail.com

## Thanks
 [@FichteFoll](https://github.com/FichteFoll) to suggest add command palette support  
 [@pribilinskiy](https://github.com/pribilinskiy) to report windows menu toggle bug  
 [@spywhere](https://github.com/spywhere) to report is_check error in some case views are not inited  
 [@Kl0tl](https://github.com/Kl0tl) to add support for horizontal scroll and implement the configureable staus bar text, Thanks!  
 [@getify](https://github.com/getify) and [@CSester](https://github.com/CSester) to report st2 activate bug

## TODO

* add context menu support.
* improve sync scroll delay.

### Please use github to submit Bugs and Feature Requests.
