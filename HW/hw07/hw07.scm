(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
  
)

(define (caddr s)
  (car (cdr (cdr s)))
  
)

(define (sign x)
  (cond ((> x 0) 1)
        ((= x 0) 0)
        (else -1))
  
)

(define (square x) (* x x))

(define (pow b n)
  (cond ((= n 0) 1)
        ((even? n) (square (pow b (/ n 2))))
        (else (* b (pow b (- n 1))))
        )
)

(define (ordered? s)
  (cond ((or (null? s) (null? (cdr s))) #t)
        ((<= (car s) (cadr s)) (ordered? (cdr s)))
        (else #f)
    )

)

(define (nodots s)
  (cond ((null? s) s)
        ((number? (car s)) (cond ((number? (cdr s)) (cons (car s) (cons (cdr s) nil)))
                                 (else (cons (car s) (nodots (cdr s))))))
         
        ((number? (cdr s)) (cons (nodots (car s)) (cons (cdr s) nil)))
        (else (cons (nodots (car s)) (nodots (cdr s))))
  )     
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((= v (car s)) #t)
          ((> (car s) v) #f)
          (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((contains? s v) (cons (car s) (cdr s)))
          ((< (car s) v) (cons (car s) (add (cdr s) v)))
          (else (cons v s))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          (else (cond ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
                      ((< (car s) (car t)) (intersect (cdr s) t))
                      (else (intersect s (cdr t)))
                      )))
          )

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((contains? t (car s)) (union (cdr s) t))
          (else (add (union (cdr s) t) (car s)))
          ))


; Binary search trees

; A data abstraction for binary trees where nil represents the empty tree
(define (tree entry left right) (list entry left right))
(define (entry t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf entry) (tree entry nil nil))
(define (leaf? t) (and (null? (right t)) (null? (left t))))

(define (in? t v)
    (cond ((empty? t) false)
          ((= (entry t) v) #t)
          (else (or (in? (left t) v) (in? (right t) v)))
          ))

; Equivalent Python code, for your reference:
;
; def contains(s, v):
;     if s.is_empty:
;         return False
;     elif s.entry == v:
;         return True
;     elif s.entry < v:
;         return contains(s.right, v)
;     elif s.entry > v:
;         return contains(s.left, v)

; (define (sort s)
;     (cond ((empty? s) nil)
;           ((< (car s) (cadr s)) (cons (car s) (sort (cdr s))))
;           (else (cons (cadr s) (cons (car s) (sort (cddr s)))))
; )
;   )

(define (as-list t)
    (define (extend t s)
        (cond ((empty? t) nil)
              ((leaf? t) (add s (entry t)))
              ; ((empty? (right t)) (add s  (extend (left t)) (cons (entry t) nil)))
              ; ((empty? (left t)) (cons (entry t) (as-list (left t))))
              ; (else (cons (as-list (left t)) (cons (entry t) (cons (as-list (right t)) nil)))
              (else (add (union (as-list (left t)) (as-list (right t))) (entry t)))
          ))
        (extend t nil)
    )

