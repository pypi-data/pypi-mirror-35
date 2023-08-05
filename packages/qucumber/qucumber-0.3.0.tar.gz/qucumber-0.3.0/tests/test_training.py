# Copyright 2018 PIQuIL - All Rights Reserved

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


import os.path
import unittest
import pytest

import numpy as np
import torch
from torch.nn.utils import parameters_to_vector

import qucumber
import qucumber.utils.data as data
import qucumber.utils.training_statistics as ts
import qucumber.utils.unitaries as unitaries
from qucumber.callbacks import MetricEvaluator, LambdaCallback
from qucumber.nn_states import ComplexWavefunction, PositiveWavefunction
from . import __tests_location__

SEED = 1234


devices = [
    pytest.param(False, id="cpu"),
    pytest.param(
        True,
        id="gpu",
        marks=[
            pytest.mark.skipif(not torch.cuda.is_available(), reason="GPU required"),
            pytest.mark.gpu,
        ],
    ),
]


@pytest.mark.parametrize("gpu", devices)
def test_positive_wavefunction(gpu):
    qucumber.set_random_seed(SEED, cpu=True, gpu=gpu, quiet=True)

    nn_state = PositiveWavefunction(10, gpu=gpu)

    old_params = parameters_to_vector(nn_state.rbm_am.parameters())

    data = torch.ones(100, 10)
    nn_state.fit(data, epochs=1, pos_batch_size=10, neg_batch_size=10)

    new_params = parameters_to_vector(nn_state.rbm_am.parameters())

    msg = "PositiveWavefunction's parameters did not change!"
    assert not torch.equal(old_params, new_params), msg


@pytest.mark.parametrize("gpu", devices)
def test_complex_wavefunction(gpu):
    qucumber.set_random_seed(SEED, cpu=True, gpu=gpu, quiet=True)
    np.random.seed(SEED)

    nn_state = ComplexWavefunction(10, gpu=gpu)

    old_params = parameters_to_vector(nn_state.rbm_am.parameters())

    data = torch.ones(100, 10)

    # generate sample bases randomly, with probability 0.9 of being 'Z', otherwise 'X'
    bases = np.where(np.random.binomial(1, 0.9, size=(100, 10)), "Z", "X")

    nn_state.fit(data, epochs=1, pos_batch_size=10, input_bases=bases)

    new_params = parameters_to_vector(nn_state.rbm_am.parameters())

    msg = "ComplexWavefunction's parameters did not change!"
    assert not torch.equal(old_params, new_params), msg


def test_complex_training_without_bases_fail():
    qucumber.set_random_seed(SEED, cpu=True, gpu=False, quiet=True)
    np.random.seed(SEED)

    nn_state = ComplexWavefunction(10, gpu=False)

    data = torch.ones(100, 10)

    msg = "Training ComplexWavefunction without providing bases should fail!"
    with pytest.raises(ValueError, message=msg):
        nn_state.fit(data, epochs=1, pos_batch_size=10, input_bases=None)


@pytest.mark.parametrize("gpu", devices)
def test_stop_training(gpu):
    qucumber.set_random_seed(SEED, cpu=True, gpu=gpu, quiet=True)
    np.random.seed(SEED)

    nn_state = PositiveWavefunction(10, gpu=gpu)

    old_params = parameters_to_vector(nn_state.rbm_am.parameters())
    data = torch.ones(100, 10)

    nn_state.stop_training = True
    nn_state.fit(data)

    new_params = parameters_to_vector(nn_state.rbm_am.parameters())

    msg = "stop_training didn't work!"
    assert torch.equal(old_params, new_params), msg


def set_stop_training(nn_state):
    nn_state.stop_training = True


@pytest.mark.parametrize("gpu", devices)
def test_stop_training_in_batch(gpu):
    qucumber.set_random_seed(SEED, cpu=True, gpu=gpu, quiet=True)
    np.random.seed(SEED)

    nn_state = PositiveWavefunction(10, gpu=gpu)

    data = torch.ones(100, 10)

    callbacks = [
        LambdaCallback(on_batch_end=lambda nn_state, ep, b: set_stop_training(nn_state))
    ]

    nn_state.fit(data, callbacks=callbacks)

    msg = "stop_training wasn't set!"
    assert nn_state.stop_training, msg


@pytest.mark.parametrize("gpu", devices)
def test_stop_training_in_epoch(gpu):
    qucumber.set_random_seed(SEED, cpu=True, gpu=gpu, quiet=True)
    np.random.seed(SEED)

    nn_state = PositiveWavefunction(10, gpu=gpu)

    data = torch.ones(100, 10)

    callbacks = [
        LambdaCallback(on_epoch_end=lambda nn_state, ep: set_stop_training(nn_state))
    ]

    nn_state.fit(data, callbacks=callbacks)

    msg = "stop_training wasn't set!"
    assert nn_state.stop_training, msg


class TestExamples(unittest.TestCase):
    @pytest.mark.slow
    def test_trainingpositive(self):
        print("Positive Wavefunction")
        print("---------------------")

        train_samples_path = os.path.join(
            __tests_location__,
            "..",
            "examples",
            "Tutorial1_TrainPosRealWavefunction",
            "tfim1d_data.txt",
        )
        psi_path = os.path.join(
            __tests_location__,
            "..",
            "examples",
            "Tutorial1_TrainPosRealWavefunction",
            "tfim1d_psi.txt",
        )

        train_samples, target_psi = data.load_data(train_samples_path, psi_path)

        nv = nh = train_samples.shape[-1]

        fidelities = []
        KLs = []

        epochs = 5
        batch_size = 100
        num_chains = 200
        CD = 10
        lr = 0.1
        log_every = 5

        print("Training 10 times and checking fidelity and KL at 5 epochs...\n")
        for i in range(10):
            print("Iteration: ", i + 1)

            nn_state = PositiveWavefunction(num_visible=nv, num_hidden=nh, gpu=False)

            space = nn_state.generate_hilbert_space(nv)
            callbacks = [
                MetricEvaluator(
                    log_every,
                    {"Fidelity": ts.fidelity, "KL": ts.KL},
                    target_psi=target_psi,
                    space=space,
                    verbose=True,
                )
            ]

            self.initialize_posreal_params(nn_state)

            nn_state.fit(
                data=train_samples,
                epochs=epochs,
                pos_batch_size=batch_size,
                neg_batch_size=num_chains,
                k=CD,
                lr=lr,
                time=True,
                progbar=False,
                callbacks=callbacks,
            )

            fidelities.append(ts.fidelity(nn_state, target_psi, space).item())
            KLs.append(ts.KL(nn_state, target_psi, space).item())

        print("\nStatistics")
        print("----------")
        print(
            "Fidelity: ",
            np.average(fidelities),
            "+/-",
            np.std(fidelities) / np.sqrt(len(fidelities)),
            "\n",
        )
        print("KL: ", np.average(KLs), "+/-", np.std(KLs) / np.sqrt(len(KLs)), "\n")

        self.assertTrue(abs(np.average(fidelities) - 0.85) < 0.02)
        self.assertTrue(abs(np.average(KLs) - 0.29) < 0.05)
        self.assertTrue((np.std(fidelities) / np.sqrt(len(fidelities))) < 0.01)
        self.assertTrue((np.std(KLs) / np.sqrt(len(KLs))) < 0.01)

    @pytest.mark.slow
    def test_trainingcomplex(self):
        print("Complex Wavefunction")
        print("--------------------")

        train_samples_path = os.path.join(
            __tests_location__,
            "..",
            "examples",
            "Tutorial2_TrainComplexWavefunction",
            "qubits_train.txt",
        )
        train_bases_path = os.path.join(
            __tests_location__,
            "..",
            "examples",
            "Tutorial2_TrainComplexWavefunction",
            "qubits_train_bases.txt",
        )
        bases_path = os.path.join(
            __tests_location__,
            "..",
            "examples",
            "Tutorial2_TrainComplexWavefunction",
            "qubits_bases.txt",
        )
        psi_path = os.path.join(
            __tests_location__,
            "..",
            "examples",
            "Tutorial2_TrainComplexWavefunction",
            "qubits_psi.txt",
        )

        train_samples, target_psi, train_bases, bases = data.load_data(
            train_samples_path, psi_path, train_bases_path, bases_path
        )

        unitary_dict = unitaries.create_dict()
        nv = nh = train_samples.shape[-1]

        fidelities = []
        KLs = []

        epochs = 5
        batch_size = 50
        num_chains = 10
        CD = 10
        lr = 0.1
        log_every = 5

        print("Training 10 times and checking fidelity and KL at 5 epochs...\n")
        for i in range(10):
            print("Iteration: ", i + 1)

            nn_state = ComplexWavefunction(
                unitary_dict=unitary_dict, num_visible=nv, num_hidden=nh, gpu=False
            )

            space = nn_state.generate_hilbert_space(nv)
            callbacks = [
                MetricEvaluator(
                    log_every,
                    {"Fidelity": ts.fidelity, "KL": ts.KL},
                    target_psi=target_psi,
                    bases=bases,
                    space=space,
                    verbose=True,
                )
            ]

            self.initialize_complex_params(nn_state)

            nn_state.fit(
                data=train_samples,
                epochs=epochs,
                pos_batch_size=batch_size,
                neg_batch_size=num_chains,
                k=CD,
                lr=lr,
                time=True,
                input_bases=train_bases,
                progbar=False,
                callbacks=callbacks,
            )

            fidelities.append(ts.fidelity(nn_state, target_psi, space).item())
            KLs.append(ts.KL(nn_state, target_psi, space, bases=bases).item())

        print("\nStatistics")
        print("----------")
        print(
            "Fidelity: ",
            np.average(fidelities),
            "+/-",
            np.std(fidelities) / np.sqrt(len(fidelities)),
            "\n",
        )
        print("KL: ", np.average(KLs), "+/-", np.std(KLs) / np.sqrt(len(KLs)), "\n")

        self.assertTrue(abs(np.average(fidelities) - 0.38) < 0.05)
        self.assertTrue(abs(np.average(KLs) - 0.33) < 0.05)
        self.assertTrue((np.std(fidelities) / np.sqrt(len(fidelities))) < 0.01)
        self.assertTrue((np.std(KLs) / np.sqrt(len(KLs))) < 0.01)

    def initialize_posreal_params(self, nn_state):
        with open(
            os.path.join(
                __tests_location__, "data", "test_training_init_pos_params.npz"
            ),
            "rb",
        ) as f:
            x = np.load(f)
            for p in x.files:
                getattr(nn_state.rbm_am, p).data = torch.tensor(x[p]).to(
                    getattr(nn_state.rbm_am, p)
                )

    def initialize_complex_params(self, nn_state):
        with open(
            os.path.join(
                __tests_location__, "data", "test_training_init_complex_params.npz"
            ),
            "rb",
        ) as f:
            x = np.load(f)
            for p in x.files:
                if p.startswith("am"):
                    rbm = nn_state.rbm_am
                elif p.startswith("ph"):
                    rbm = nn_state.rbm_ph

                q = p.split("_", maxsplit=1)[-1]
                getattr(rbm, q).data = torch.tensor(x[p]).to(getattr(rbm, q))


if __name__ == "__main__":
    unittest.main()
