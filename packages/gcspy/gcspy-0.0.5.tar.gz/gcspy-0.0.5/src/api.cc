#include "api.hh"

#include <gcs/constraints/in.hh>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <optional>

namespace py = pybind11;
using namespace gcs;

using std::string;
using std::to_string;
using std::cout;
using std::endl;

auto APIForPython::create_integer_variable(const vector<long long int> & domain, const string& name) -> string {
    vector<Integer> domain_i(domain.begin(), domain.end());
    auto var_id = p.create_integer_variable(domain_i, name);
    return map_new_id(var_id);
}

auto APIForPython::create_integer_constant(const long long int& value) -> string {
    auto constant_id = ConstantIntegerVariableID{Integer(value)};
    return map_new_id(constant_id);
}

auto APIForPython::minimise(const string& var_id) -> void {
    p.minimise(get_var(var_id));
}

auto APIForPython::maximise(const string& var_id) -> void {
    p.maximise(get_var(var_id));
}

auto APIForPython::negate(const string &var_id) -> string {
    auto var = get_var(var_id);
    return map_new_id(-var);
}

auto APIForPython::add_constant(const string &var_id, long long int constant) -> string {
    auto var = get_var(var_id);
    return map_new_id(var + Integer{constant});
}

auto APIForPython::solve(bool all_solutions) -> std::unordered_map<string, unsigned long long int> {
    auto stats = solve_with(p,
        SolveCallbacks{
                .solution = [&](const CurrentState & s) -> bool {
                    for(auto const& var : vars) {
                        solution_values[var.second] = s(var.second).raw_value;
                    }
                    return all_solutions; // Keep searching for solutions
                },});
    std::unordered_map<string, unsigned long long int> stats_map{};
    stats_map["recursions"] = stats.recursions;
    stats_map["failures"] = stats.failures;
    stats_map["propagations"] = stats.propagations;
    stats_map["effectful_propagations"] = stats.effectful_propagations;
    stats_map["contradicting_propagations"] = stats.contradicting_propagations;
    stats_map["solutions"] = stats.solutions;
    stats_map["max_depth"] = stats.max_depth;
    stats_map["n_propagators"] = stats.n_propagators;
    stats_map["solve_time"] = stats.solve_time.count();

    return stats_map;
}

auto APIForPython::get_solution_value(const string& var_id) -> std::optional<long long int> {
    try {
        auto sol_val = solution_values.at(get_var(var_id));
        return sol_val;
    } catch(const std::out_of_range &e) {
        return std::nullopt;
    }
}

auto APIForPython::get_proof_filename() -> string {
    return proof_filename;
}

auto APIForPython::post_abs(const string &var_id_1, const string &var_id_2) -> void {
    p.post(Abs( get_var(var_id_1), get_var(var_id_2)));
}

auto APIForPython::post_arithmetic(const string &var_id_1, const string &var_id_2,
                                   const string &result_id, const string &op) -> void {
    auto var1 = get_var(var_id_1);
    auto var2 = get_var(var_id_2);
    auto result = get_var(result_id);
    if(op == "sum") {
        try {
            p.post(Plus(var1, var2, result));
        } catch (const std::runtime_error& e) {
            cout << e.what() << endl;
        }
    } else if(op == "mul") {
        p.post(Times(var1, var2, result));
    } else if(op == "div") {
        p.post(Div(var1, var2, result));
    } else if(op == "mod") {
        p.post(Mod(var1, var2, result));
    } else if(op == "pow") {
        p.post(Power(var1, var2, result));
    } else {
        throw pybind11::value_error("Invalid arithmetic operator for Glasgow Constraint Solver: '" + op + "'");
    }
}

auto APIForPython::post_alldifferent(const vector<std::string> &var_ids) -> void {
    p.post(AllDifferent{get_vars(var_ids)});
}

auto APIForPython::post_compare_less(const string &var_id_1, const string &var_id_2, bool or_equal) -> void {
    p.post(innards::CompareLessThanReif( get_var(var_id_1), get_var(var_id_2),
                                            TrueLiteral{}, false, or_equal));
}

auto APIForPython::post_compare_less_if(const string &var_id_1, const string &var_id_2, const string &reif_id,
                                          bool or_equal) -> void {
    p.post(innards::CompareLessThanReif( get_var(var_id_1), get_var(var_id_2),
                                            get_var(reif_id)!=0_i, false, or_equal));
}

auto APIForPython::post_count(const vector<string> &var_ids, const string &var_id, const string &count_id)
                                -> void {
    p.post(Count(get_vars(var_ids), get_var(var_id), get_var(count_id)));
}

auto APIForPython::post_element(const string &var_id, const string &index_id,
                                const vector<string> &var_ids) -> void {
    p.post(Element(get_var(var_id), get_var(index_id), get_vars(var_ids)));
}

auto APIForPython::post_equals(const string &var_id_1, const string &var_id_2) -> void {
    p.post(Equals(get_var(var_id_1), get_var(var_id_2)));
}

auto APIForPython::post_equals_if(const string &var_id_1, const string &var_id_2, const string &reif_id) -> void {
    p.post(EqualsIf(get_var(var_id_1), get_var(var_id_2), get_var(reif_id)!=0_i));
}

auto APIForPython::post_not_equals(const string &var_id_1, const string &var_id_2) -> void {
    p.post(NotEquals(get_var(var_id_1), get_var(var_id_2)));
}

auto APIForPython::post_in(const string &var_id, const vector<long long int> &domain) -> void {
    vector<Integer> domain_i{};
    for(auto d : domain) {
        domain_i.emplace_back(d);
    }
    p.post(In(get_var(var_id), domain_i) );
}

auto APIForPython::post_in_vars(const string &var_id, const vector<string> &var_ids) -> void {
    p.post(In(get_var(var_id), get_vars(var_ids)));
}

auto APIForPython::post_linear_equality(const vector<string> &var_ids, const vector<long long int> &coeffs,
                                        long long int value) -> void {
    p.post(LinearEquality{move(make_linear(var_ids, coeffs)), Integer{value}});
}

auto APIForPython::post_linear_lessequal(const vector<string> &var_ids, const vector<long long int> &coeffs,
                                         long long int value) -> void {
    p.post(LinearLessEqual{move(make_linear(var_ids, coeffs)), Integer{value}});
}

auto APIForPython::post_linear_greaterequal(const vector<string> &var_ids, const vector<long long int> &coeffs,
                                            long long int value) -> void {
    p.post(LinearGreaterThanEqual{move(make_linear(var_ids, coeffs)), Integer{value}});
}

auto APIForPython::post_and(const vector<string> &var_ids) -> void {
    p.post(And{get_vars(var_ids)});
}

auto APIForPython::post_and_if(const vector<string> &var_ids, const string &reif_id) -> void {
    // Note: x => AND([vars]) is equivalent to x <=> AND([vars, x])
    auto new_vars = get_vars(var_ids);
    auto reif_var = get_var(reif_id);
    new_vars.push_back(reif_var);
    p.post(And{new_vars, reif_var});
}

auto APIForPython::post_or(const vector<string> &var_ids) -> void {
    p.post(Or{get_vars(var_ids)});
}

auto APIForPython::post_or_if(const vector<string> &var_ids, const string &reif_id) -> void {
    // Note: x => OR([vars]) is equivalent to OR([vars, 1 - x])
    auto new_vars = get_vars(var_ids);
    auto reif_var = - get_var(reif_id) + 1_i;
    new_vars.push_back(reif_var);
    p.post(Or{new_vars});
}

auto APIForPython::post_implies(const string &var_id_1, const string &var_id_2) -> void {
    // Note: x => y is equivalent to OR([y, 1-x])
    auto var_1 = get_var(var_id_1);
    auto var_2 = get_var(var_id_2);
    p.post(Or{{var_2, -var_1 + 1_i}});
}

auto APIForPython::post_implies_if(const string &var_id_1, const string &var_id_2, const string &reif_id) -> void {
    // Note x => (a => b) is equivalent to OR([b, 1-a, 1-x])
    auto var_1 = get_var(var_id_1);
    auto var_2 = get_var(var_id_2);
    auto reif_var = get_var(reif_id);
    p.post(Or{{var_2, -var_1 + 1_i, -reif_var + 1_i}});
}

auto APIForPython::post_binary_xor(const string &var_id_1, const string &var_id_2) -> void {
    // Note XOR(a, b) is equivalent to the two constraints OR([a, b]), OR([1-a, 1-b])
    auto var_1 = get_var(var_id_1);
    auto var_2 = get_var(var_id_2);
    p.post(Or{{var_1, var_2}});
    p.post(Or{{-var_1 + 1_i, -var_2 + 1_i}});
}

auto APIForPython::post_binary_xor_if(const string &var_id_1, const string &var_id_2, const string &reif_id) -> void {
    // Likewise x -> XOR(a, b) is equivalent to x -> OR([a, b]), x -> OR([1 - a, 1 - b])
    // i.e. OR([a, b, 1-x]), OR([1-a, 1-b, 1-x])
    auto var_1 = get_var(var_id_1);
    auto var_2 = get_var(var_id_2);
    auto reif_var = get_var(reif_id);
    p.post(Or{{var_1, var_2, - reif_var + 1_i}});
    p.post(Or{{- var_1 + 1_i, - var_2 + 1_i, - reif_var + 1_i}});

}


auto APIForPython::post_min(const vector<string>& var_ids, const string& var_id) -> void {
    p.post(ArrayMin(get_vars(var_ids), get_var(var_id)));
}

auto APIForPython::post_max(const vector<string> &var_ids, const string& var_id) -> void {
    p.post(ArrayMax(get_vars(var_ids), get_var(var_id)));
}

auto APIForPython::post_nvalue(const string &var_id, const vector<string> &var_ids) -> void {
    p.post(NValue(get_var(var_id), get_vars(var_ids)));
}

auto APIForPython::post_table(const vector<string> &var_id, const vector<vector<long long int>> &table) -> void {
    SimpleTuples table_i;
    for(const auto& v : table) {
        vector<Integer> row{};
        for(auto vv : v) {
            row.emplace_back(vv);
        }
        table_i.push_back(row);
    }

    //Clangd doesn't like this for some reason, but it compiles with g++-12 (and others)
    p.post(Table(get_vars(var_id), move(table_i)));
}

/**
 * Python bindings: match the API exactly, using automatic STL conversion provided by Pybind11.
 */
PYBIND11_MODULE(gcspy, m) {
m.doc() = "Python bindings for the Glasgow Constraint Solver";
py::class_<APIForPython>(m, "GlasgowConstraintSolver")
.def(py::init<>())
.def("create_integer_variable", &APIForPython::create_integer_variable)
.def("create_integer_constant", &APIForPython::create_integer_constant)
.def("maximise", &APIForPython::maximise)
.def("minimise", &APIForPython::minimise)
.def("negate", &APIForPython::negate)
.def("add_constant", &APIForPython::add_constant)
.def("solve", &APIForPython::solve, py::arg("all_solutions") = true)

.def("get_solution_value", &APIForPython::get_solution_value)
.def("get_proof_filename", &APIForPython::get_proof_filename)

// Constraints
.def("post_abs", &APIForPython::post_abs)
.def("post_alldifferent", &APIForPython::post_alldifferent)
.def("post_arithmetic", &APIForPython::post_arithmetic)
.def("post_compare_less", &APIForPython::post_compare_less)
.def("post_compare_less_if", &APIForPython::post_compare_less_if)
.def("post_count", &APIForPython::post_count)
.def("post_element", &APIForPython::post_element)
.def("post_equals", &APIForPython::post_equals)
.def("post_equals_if", &APIForPython::post_equals_if)
.def("post_not_equals", &APIForPython::post_not_equals)
.def("post_in", &APIForPython::post_in)
.def("post_in_vars", &APIForPython::post_in_vars)
.def("post_linear_equality", &APIForPython::post_linear_equality)
.def("post_linear_lessequal", &APIForPython::post_linear_lessequal)
.def("post_linear_greaterequal", &APIForPython::post_linear_greaterequal)
.def("post_and", &APIForPython::post_and)
.def("post_and_if", &APIForPython::post_and_if)
.def("post_or", &APIForPython::post_or)
.def("post_or_if", &APIForPython::post_or_if)
.def("post_implies", &APIForPython::post_implies)
.def("post_implies_if", &APIForPython::post_implies_if)
.def("post_binary_xor", &APIForPython::post_binary_xor)
.def("post_binary_xor_if", &APIForPython::post_binary_xor_if)
.def("post_min", &APIForPython::post_min)
.def("post_max", &APIForPython::post_max)
.def("post_nvalue", &APIForPython::post_nvalue)
.def("post_table", &APIForPython::post_table)
;
}
