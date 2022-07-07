# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_example_spec_file

%define debug_package %{nil}

%define _name hassmpris

%define mybuildnumber %{?build_number}%{?!build_number:1}

Name:           python-%{_name}
Version:        0.1.13
Release:        %{mybuildnumber}%{?dist}
Summary:        Linux desktop multimedia integration with Home Assistant

License:        LGPLv2.1
URL:            https://github.com/Rudd-O/%{_name}
Source:         %{url}/archive/v%{version}/%{_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel, python-types-cryptography, openssl

%global _description %{expand:
This package contains a kit that allows you to develop clients and servers
that authenticate to each other mutually, issuing certificates to clients that
can then be used for secure mutual TLS or gRPC authenticated communication.}

%description %_description

%package -n python3-%{_name}
Summary:        %{summary}

%description -n python3-%{_name} %_description

%prep
%autosetup -p1 -n %{_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{_name}


%check
%tox


# Note that there is no %%files section for
# the unversioned python module, python-pello.

# For python3-pello, %%{pyproject_files} handles code files and %%license,
# but executables and documentation must be listed in the spec file:

%files -n python3-%{_name} -f %{pyproject_files}
%doc README.md


%changelog
* Thu Jun 16 2022 Manuel Amador <rudd-o@rudd-o.com> 0.1.0-1
- First RPM packaging release
