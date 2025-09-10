import numpy as np
import matplotlib.pyplot as plt

def dexp_true(t):
    return np.exp(t)

def fd_exp(t,h):
    val = (np.exp(t+h) - np.exp(t) ) / h
    return val

def cd_exp(t,h):
    val = (np.exp(t+h/2) - np.exp(t-h/2) ) / h
    return val

def ed_exp(t,h):
    val = (8*( np.exp(t+h/4) - np.exp(t-h/4) ) - ( np.exp(t+h/2) - np.exp(t-h/2) ))/3/h
    return val

def rel_error(approx, true):
    return np.abs((approx - true)/true) 

if __name__ == "__main__":

    t_val=[0.1,1,100]

    fig, axs = plt.subplots(2,3, gridspec_kw={'height_ratios':[1.5,2]}, figsize=(20,10))

    # initialize values and empty lists in preparation
    for i,t in enumerate(t_val):
        true_exp_val = dexp_true(t)
        h_vals = []
        fd_exp_vals, cd_exp_vals, ed_exp_vals = [],[],[]
        fd_exp_errs, cd_exp_errs, ed_exp_errs = [],[],[]

        h=1.0 # initializes h for next nested loop

        for h in np.logspace(-16, 0.5, 500): # logspace makes the iteration space nicer. lowest value should be machine precision for a 64-bit float
            h_vals.append(h)

            fd_exp_vals.append(fd_exp(t,h))
            cd_exp_vals.append(cd_exp(t,h))
            ed_exp_vals.append(ed_exp(t,h))

            fd_exp_errs.append(rel_error(fd_exp(t,h),true_exp_val))
            cd_exp_errs.append(rel_error(cd_exp(t,h),true_exp_val))
            ed_exp_errs.append(rel_error(ed_exp(t,h),true_exp_val))

            h/2 # makes h smaller for next loop

        # promote lists to np arrays
        h_vals=np.array(h_vals)

        fd_exp_vals=np.array(fd_exp_vals)
        cd_exp_vals=np.array(cd_exp_vals)
        ed_exp_vals=np.array(ed_exp_vals)

        fd_exp_errs=np.array(fd_exp_errs)
        cd_exp_errs=np.array(cd_exp_errs)
        ed_exp_errs=np.array(ed_exp_errs)

        # BEGIN PLOTS

        # top row
        ax_top = axs[0,i] #give name for simplicity
        ax_top.xaxis.grid(True)
        ax_top.yaxis.grid(True)
        ax_top.axhline(true_exp_val, c='r', lw=1, linestyle="-", label='True' )
        ax_top.plot(h_vals, fd_exp_vals, c='g', ls='--', label='Forward')
        ax_top.plot(h_vals, cd_exp_vals, c='b', ls=':', label='Central')
        ax_top.plot(h_vals, ed_exp_vals, c='m', ls='-.', label='Extrapolated')
        ax_top.set_xscale('log')
        ax_top.set_ylabel(r"$\frac{d}{dt}[\exp(t)]$", fontsize=14)
        ax_top.set_title(f"t={t}")
        ax_top.legend()

        #bottom row
        ax_bot = axs[1,i]
        ax_bot.xaxis.grid(True)
        ax_bot.yaxis.grid(True)
        ax_bot.plot(h_vals, fd_exp_errs, c='g', ls='--', label='Forward')
        ax_bot.plot(h_vals, cd_exp_errs, c='b', ls=':', label='Central')
        ax_bot.plot(h_vals, ed_exp_errs, c='m', ls='-.', label='Extrapolated')
        ax_bot.set_xscale('log')
        ax_bot.set_yscale('log')
        ax_bot.set_xlabel('h', fontsize=15)
        ax_bot.set_ylabel(r'$\varepsilon_{rel}$', fontsize=20)
        ax_bot.legend()

    plt.savefig("exp.png",dpi=300)