// ok: eval-with-expression
eval('alert')

// ruleid: eval-with-expression
eval(user_input)

// ok: eval-with-expression
window.eval('alert')

// ruleid: eval-with-expression
window.eval(user_input)

// ok: eval-with-expression
var x = Function('a', 'b', 'return 1')

// ruleid: eval-with-expression
var x = Function('a', 'b', user_input)

// ok: eval-with-expression
var x = new Function('a', 'b', 'return 1')

// ruleid: eval-with-expression
var x = new Function('a', 'b', user_input)

// ruleid: eval-with-expression
eval('alert(' + c + ')')

// ruleid: eval-with-expression
eval(`return ${funcName}(a,b)`)

var f = "return 1"
// ok: eval-with-expression
var x = new Function('a', 'b', f)
