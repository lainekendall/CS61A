 # Combinations
    if not scheme_listp(expr):
        raise SchemeError("malformed list: {0}".format(str(expr)))
    first, rest = expr.first, expr.second
    "*** YOUR CODE HERE ***"
    if scheme_symbolp(first) and first in SPECIAL_FORMS:
        result = SPECIAL_FORMS[first](rest, env)
    else:
        procedure = scheme_eval(first, env)
        args = rest.map(lambda operand: scheme_eval(operand, env))
        result = scheme_apply(procedure, args, env)
    return result


     (define (firsts pairs)
    (cond ((null? pairs) nil)
          (else (cons (caar pairs) (firsts (cdr pairs))))
    ))

(define (seconds pairs)
    (cond ((null? pairs) nil)
          (else (cons (cadar pairs) (seconds (cdr pairs))))
    ))

    (cond ((null? pairs) (cons nil (cons nil nil)))
          (else (cons (firsts pairs) (cons (seconds pairs) nil)))
  ))