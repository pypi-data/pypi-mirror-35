import NoisyEvolution as ne
import numpy as np
import Operations as op
from scipy.linalg import expm
import Gates as g
from lea import *
from qutip import *
from matplotlib.pyplot import *
import SpecialStates as ss

class Qubit(object):

    def __init__(self, value):
        """
        :param state: Should be 0 or 1. If 0 qubit initialized to ground state if 1 qubit initialized to excited state
        :return: Returns the state of the qubit
        """
        if value == 0:
            self.state = np.array([[1, 0], [0, 0]])
        elif value == 1:
            self.state = np.array([[0, 0], [0, 1]])
        else:
            print("Please enter 0 or 1 only !")

    def q_evolve(self, h, dt):
        """
        :param h: Hamiltonian by which to evolve the system
        :param dt: time step to evolve by
        :return: returns the state of qubit after evolution
        """
        U = expm(-1j*h*dt)
        self.state = np.dot(U, np.dot(self.state, op.ctranspose(U)))

    def q_decohere(self, k):
        """
        :param k: A set of kraus operators for decoherent evolutioin
        :param n: This is the number of qubits
        :return: Returns the state of the qubit after application of kraus operators
        """
        self.state = ne.decohere(k, self.state, 1)

    def operator(self, o):
        """
        :param o: The operator you want applied to the qubit
        :return:  Returns the transformed density matrix after the operation
        """
        self.state = np.dot(o, np.dot(self.state, op.ctranspose(o)))

    def measure(self):
        """
        :return: Density matrix after a measurement
        """
        p0 = np.trace(np.dot(self.state, g.b1()))
        p1 = np.trace(np.dot(self.state, g.b4()))
        outcome = {'0': p0*100, '1': p1*100}
        picked_obj = Lea.fromValFreqsDict(outcome)
        picked_state = picked_obj.random()

        if picked_state == '0':
            self.state = g.b1()
        else:
            self.state = g.b4()


class MultiQubit(Qubit):
    def __init__(self, string):
        """
        :param string: This should be a string of 1's and 0's where 1 is the |1> and
        0 is |0>
        :return: Returns the
        """
        tmp = 1
        for i in range(0, len(string)):
            if string[i] == '0':
                tmp = np.kron(tmp, np.array([[1, 0], [0, 0]]))
            else:
                tmp = np.kron(tmp, np.array([[0, 0], [0, 1]]))
        self.state = tmp

    def q_decohere(self, k, n):
        self.state = ne.decohere(k, self.state, n)


class QubitObj(object):
    """
    Does what the Qubit object and multi qubit object class do but using
    qutip stuff. If you want to use qutip, this class automizes alot of stuff
    """
    def __init__(self, n, t1_list, t2_list, t3_list, string='', damp=True, phase_damp=True, finite_temp=False,
                 identical_bath=True):
        q0 = basis(2, 0)
        q1 = basis(2, 1)
        self.opt = Options(rhs_reuse=True, store_states=True)
        q_list = []
        q_list1 = []
        if isinstance(string, str):
            for c in string:
                if c == '0':
                    q_list.append(q0)
                    q_list1.append(q0 * q0.dag())
                    self.psi = tensor(*q_list)
                    self.rho = tensor(*q_list1)
                elif c == '1':
                    q_list.append(q1)
                    q_list1.append(q1 * q1.dag())
                    self.rho = tensor(*q_list1)
                    self.psi = tensor(*q_list)
        self.hamiltonian = 0
        self.psi_results = 0
        self.rho_results = 0
        self.operators = []
        self.c_op = {}
        self.dephase_op = {}
        self.create_op = {}
        self.collap = []
        self.x_label = ''
        self.y_label = ''
        self.label = ''
        self.x_axis = []
        self.y_axis = []
        self.n = n
        self.t1 = t1_list
        self.t2 = t2_list
        self.t3 = t3_list
        self.times = 0
        self.annihilate = {'0': qeye(2), '1': destroy(2)}
        self.create = {'0': qeye(2), '1': create(2)}
        self.dephase = {'0': qeye(2), '1': sigmaz()}
        self.final_state= 0
        for i in range(0, n):
            self.c_op[str(i)] = []
            self.create_op[str(i)] =[]
            self.dephase_op[str(i)] = []
        self.noise_op(same_bath=identical_bath, relax=damp, dephase=phase_damp, create=finite_temp)

    def evolve(self):
        self.psi_results = mesolve(self.hamiltonian, self.psi, self.times, [], self.operators, options=self.opt)
        self.rho_results = mesolve(self.hamiltonian, self.rho, self.times, self.collap, self.operators, options=self.opt)
        self.final_state = self.rho_results.states[-1].full()

    def apply_op(self, op):
        self.psi = op * self.psi
        self.rho = op * self.rho * op.dag()

    def graph(self, *args):
        xlabel(self.x_label)
        ylabel(self.y_label)
        plot(*args, label=self.label)
        legend()
        show()

    def noise_op(self, same_bath=True, relax=True, dephase=False,create=False):
        noise_op_string_list = op.generatehamiltoniantring(self.n, '1')
        for qubit, string in enumerate(noise_op_string_list):
            for char in string:
                self.c_op[str(qubit)].append(self.annihilate[char])
                self.dephase_op[str(qubit)].append(self.dephase[char])
                self.create_op[str(qubit)].append(self.create[char])
        for q, q1, q2 in zip(self.c_op, self.dephase_op, self.create_op):
            if relax:
                self.c_op[q] = tensor(*self.c_op[q])
            if dephase:
                self.dephase_op[q1] = tensor(*self.dephase_op[q1])
            if create:
                self.create_op[q2] = tensor(*self.create_op[q2])
                self.collap.append(self.create_op[q2])
        if same_bath:
            if relax:
                for qs in self.c_op:
                    self.c_op[qs] = np.sqrt(1/self.t1[0])*self.c_op[qs]
                    self.collap.append(self.c_op[qs])
            if dephase:
                for qs in self.dephase_op:
                    self.dephase_op[qs] = np.sqrt(1/(2*self.t2[0]))*self.dephase_op[qs]
                    self.collap.append(self.dephase_op[qs])
            if create:
                for qs in self.dephase_op:
                    self.create_op[qs] = np.sqrt(1/(self.t3[0]))* self.create_op[qs]
                    self.collap.append(self.create_op[qs])
        if same_bath is False:
            if relax:
                for t1_list, qs in enumerate(self.c_op):
                    self.c_op[qs] = np.sqrt(1/self.t1[t1_list])*self.c_op[qs]
                    self.collap.append(self.c_op[qs])
            if dephase:
                for t2_list, qs in enumerate(self.dephase_op):
                    self.dephase_op[qs] = np.sqrt(1/(2*self.t2[t2_list]))*self.dephase_op[qs]
                    self.collap.append(self.dephase_op[qs])
            if create:
                for t3_list, qs in enumerate(self.create_op):
                    self.create_op[qs] = np.sqrt(1/self.t3[t3_list])*self.create_op[qs]
                    self.collap.append(self.create_op[qs])


if __name__ == '__main__':

     q = QubitObj(4, [0.5, 0.3], [0.5, 0.6], [10**(-9), 10**(-9)], string='1111',
                  identical_bath=True)
     q.times = np.linspace(0, 1, 10000)
     q.hamiltonian = tensor(sigmaz(), sigmaz(), sigmaz(),sigmaz())
     q.operators.append(tensor(sigmay(), sigmay(),sigmay(), sigmay()))
     q.rho = ss.cluster_obj(4, density_matrix=True)
     q.x_axis = q.times
     q.evolve()
     print(q.rho_results.expect[0])
     q.y_axis = q.rho_results.expect[0]
     q.label = 'Probability of $\sigma_z$'
     q.graph(q.times, q.y_axis)












