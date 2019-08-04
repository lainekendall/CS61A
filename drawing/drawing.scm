

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (box func1 dist func2 angle k max start_color)

	(define (repeat func1 dist func2 angle k counter)
		(cond 
			((> counter 0) (begin (random_repeat func1 dist k start_color) (func2 angle) (repeat func1 dist func2 angle k (- counter 1))))
			(else (func1 .0001))))

	(cond ((= max 0) (bgcolor (rgb 1 1 1)))
		  (else (begin (repeat func1 dist func2 angle k 2) (box func1 dist func2 angle (+ k 1) (- max 1) start_color)))))
	
		
(define (random_repeat func arg k start_color)
	(cond ((= 0 k) (func arg))
		  (else (begin (bgcolor start_color) (func arg) (random_repeat func arg (- k 1) (cycle start_color)))
		)))


(define (cycle start)
	(cond ((eq? start (rgb 1 1 1)) (define start (rgb 1 .9 .9)) start)
		((eq? start (rgb 1 .9 .9)) (define start (rgb 1 .8 .8)) start)
		((eq? start (rgb 1 .8 .8)) (define start (rgb 1 .7 .7)) start)
		((eq? start (rgb 1 .7 .7)) (define start (rgb 1 .6 .6)) start)
		((eq? start (rgb 1 .6 .6)) (define start (rgb 1 .5 .5)) start)
		((eq? start (rgb 1 .5 .5)) (define start (rgb 1 .3 .3)) start)
		((eq? start (rgb 1 .3 .3)) (define start (rgb 1 .1 .1)) start)
		((eq? start (rgb 1 .1 .1)) (define start (rgb 1 0 0)) start)
		((eq? start (rgb 1 0 0)) (define start (rgb .9 0 .1)) start)
		((eq? start (rgb .9 0 .1)) (define start (rgb .8 0 .2)) start)
		((eq? start (rgb .8 0 .2)) (define start (rgb .7 0 .3)) start)
		((eq? start (rgb .7 0 .3)) (define start (rgb .6 0 .4)) start)
		((eq? start (rgb .6 0 .4)) (define start (rgb .5 0 .5)) start)
		((eq? start (rgb .5 0 .5)) (define start (rgb .4 0 .6)) start)
		((eq? start (rgb .4 0 .6)) (define start (rgb .3 0 .7)) start)
		((eq? start (rgb .3 0 .7)) (define start (rgb .2 0 .8)) start)
		((eq? start (rgb .2 0 .8)) (define start (rgb .1 0 .9)) start)
		((eq? start (rgb .1 0 .9)) (define start (rgb 0 0 1)) start)
		((eq? start (rgb 0 0 1)) (define start (rgb 0 .1 .9)) start)
		((eq? start (rgb 0 .1 .9)) (define start (rgb 0 .2 .8)) start)
		((eq? start (rgb 0 .2 .8)) (define start (rgb 0 .3 .7)) start)
		((eq? start (rgb 0 .3 .7)) (define start (rgb 0 .4 .6)) start)
		((eq? start (rgb 0 .4 .6)) (define start (rgb 0 .5 .5)) start)
		((eq? start (rgb 0 .5 .5)) (define start (rgb 0 .6 .4)) start)
		((eq? start (rgb 0 .6 .4)) (define start (rgb 0 .7 .3)) start)
		((eq? start (rgb 0 .7 .3)) (define start (rgb 0 .8 .2)) start)
		((eq? start (rgb 0 .8 .2)) (define start (rgb 0 .9 .1)) start)
		((eq? start (rgb 0 .9 .1)) (define start (rgb 0 1 0)) start)
		((eq? start (rgb 0 1 0)) (define start (rgb 1 1 1)) start)))


	; (cond ((eq? start (rgb 0 0 1)) (define start (rgb 1 0 1)) start)		; blue to pink
	; 	((eq? start (rgb 1 0 1)) (define start (rgb .3 .6 .8)) start)		; pink to light blue
	; 	((eq? start (rgb .3 .6 .8)) (define start (rgb .5 0 .5)) start)		; light blue to purple
	; 	((eq? start (rgb .5 0 .5)) (define start (rgb 0 1 1)) start)		; purple to bright teal
	; 	((eq? start (rgb 0 1 1)) (define start (rgb .5 0 0)) start)			; to dark red
	; 	((eq? start (rgb .5 0 0)) (define start (rgb 0 .5 .5)) start)		; to green
	; 	((eq? start (rgb 0 .5 .5)) (define start (rgb 0 0 1)) start)))		; to dark blue

(box fd 10 rt 90 2 56 (rgb 1 1 1))

; fd, rt fd, rt      == 	k = 1   counter = 2
; fd, fd, rt, fd, fd, rt  k = 2 	counter = 2
; fd, fd, fd, rt, 		k = 3	counter = 2

























